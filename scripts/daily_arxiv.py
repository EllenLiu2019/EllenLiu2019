import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import datetime
import os

try:
    from openai import OpenAI
    DEEPSEEK_AVAILABLE = True
except ImportError:
    DEEPSEEK_AVAILABLE = False
    print("Warning: openai library not installed. Chinese translation will be skipped.")
    print("Install it with: pip install openai")

def fetch_papers(query="cat:cs.CL", max_results=5):
    """
    Fetch latest papers from ArXiv API.
    Default query is cs.CL (Computation and Language) for LLM/NLP papers.
    """
    base_url = 'http://export.arxiv.org/api/query?'
    # Sort by submittedDate descending to get latest
    # Encode the query to handle spaces and special characters
    encoded_query = urllib.parse.quote(query)
    url = f'{base_url}search_query={encoded_query}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}'
    
    try:
        # Create SSL context to handle certificate issues (for local testing)
        import ssl
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        response = urllib.request.urlopen(url, context=ssl_context)
        data = response.read().decode('utf-8')
        root = ET.fromstring(data)
        
        papers = []
        # Namespace for atom format
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns).text.replace('\n', ' ').strip()
            summary = entry.find('atom:summary', ns).text.replace('\n', ' ').strip()
            link = entry.find('atom:id', ns).text
            published = entry.find('atom:published', ns).text[:10]  # YYYY-MM-DD
            
            papers.append({
                'title': title,
                'summary': summary,
                'link': link,
                'date': published
            })
            
        return papers
    except Exception as e:
        print(f"Error fetching papers: {e}")
        return []

def translate_text(text, api_key=None):
    """
    Translate text using DeepSeek API.
    Translates English to Simplified Chinese with technical terminology preserved.
    """
    if not DEEPSEEK_AVAILABLE:
        return text
    
    if not api_key:
        api_key = os.getenv('DEEPSEEK_API_KEY')
        if not api_key:
            print("Warning: DEEPSEEK_API_KEY not set. Skipping translation.")
            return text
    
    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional translator specializing in AI and computer science papers. Translate the following text from English to Simplified Chinese. Preserve technical terms and maintain the original meaning accurately."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0.3,  # Lower temperature for more consistent translation
            max_tokens=2000   # Sufficient for full summaries
        )
        
        translated = response.choices[0].message.content.strip()
        return translated
    except Exception as e:
        print(f"DeepSeek translation error: {e}")
        return text  # Return original if translation fails

def generate_markdown(papers, lang='en'):
    """
    Generate markdown content for the papers.
    lang: 'en' for English, 'zh' for Chinese
    """
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    if lang == 'zh':
        md_content = f"**更新日期: {current_date}**\n\n"
        if not papers:
            md_content += "今日未发现新论文。\n"
            return md_content
    else:
        md_content = f"**Updated on: {current_date}**\n\n"
        if not papers:
            md_content += "No new papers found today.\n"
            return md_content

    for i, paper in enumerate(papers, 1):
        if lang == 'zh':
            # Translate title and full summary using DeepSeek
            api_key = os.getenv('DEEPSEEK_API_KEY')
            translated_title = translate_text(paper['title'], api_key)
            # Translate the complete summary, not truncated
            translated_summary = translate_text(paper['summary'], api_key)
            
            md_content += f"### {i}. [{translated_title}]({paper['link']})\n"
            md_content += f"- **摘要**: {translated_summary}\n\n"
        else:
            # For English, show full summary
            md_content += f" {i}. [{paper['title']}]({paper['link']})\n"
        
    return md_content

def update_readme(file_path, new_content):
    """
    Update the README file between markers.
    """
    start_marker = "<!-- DAILY_ARXIV_SUMMARY_START -->"
    end_marker = "<!-- DAILY_ARXIV_SUMMARY_END -->"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if start_marker not in content or end_marker not in content:
            print(f"Markers not found in {file_path}")
            return
            
        start_idx = content.find(start_marker) + len(start_marker)
        end_idx = content.find(end_marker)
        
        updated_content = (
            content[:start_idx] + 
            "\n" + new_content + 
            content[end_idx:]
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        print(f"Successfully updated {file_path}")
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def save_papers_to_file(papers, lang='en', api_key=None):
    """
    Save papers to a file in data/zh/ or data/en/ directory.
    Format: YYYYMMDD.md (e.g., 20251202.md)
    """
    # Determine subdirectory based on language
    subdir = "zh" if lang == 'zh' else "en"
    data_dir = os.path.join("data", subdir)
    
    # Create directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")
    
    # Format date as YYYYMMDD
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    filename = os.path.join(data_dir, f"{current_date}.md")
    
    try:
        # Format date for display (YYYY-MM-DD)
        display_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        with open(filename, 'w', encoding='utf-8') as f:
            if lang == 'zh':
                f.write(f"# 每日论文速递 - {display_date}\n\n")
                f.write(f"**更新日期**: {display_date}\n\n")
                f.write("---\n\n")
            else:
                f.write(f"# Daily ArXiv Papers - {display_date}\n\n")
                f.write(f"**Updated on**: {display_date}\n\n")
                f.write("---\n\n")
            
            for i, paper in enumerate(papers, 1):
                if lang == 'zh':
                    # Translate title and summary
                    translated_title = translate_text(paper['title'], api_key)
                    translated_summary = translate_text(paper['summary'], api_key)
                    
                    f.write(f"## {i}. {translated_title}\n\n")
                    f.write(f"- **原文链接**: {paper['link']}\n")
                    f.write(f"- **发布日期**: {paper['date']}\n")
                    f.write(f"- **摘要**:\n\n{translated_summary}\n\n")
                    f.write("---\n\n")
                else:
                    f.write(f"## {i}. {paper['title']}\n\n")
                    f.write(f"- **Link**: {paper['link']}\n")
                    f.write(f"- **Published Date**: {paper['date']}\n")
                    f.write(f"- **Abstract**:\n\n{paper['summary']}\n\n")
                    f.write("---\n\n")
        
        print(f"Successfully saved papers to {filename}")
        return filename
    except Exception as e:
        print(f"Error saving papers to file: {e}")
        return None

if __name__ == "__main__":
    # Keywords: LLM, RAG, FinTech, AI Architect
    # Constructing a query for relevant papers
    query = 'cat:cs.CL AND (all:LLM OR all:RAG OR all:Agentic)' 
    
    papers = fetch_papers(query=query, max_results=3)
    api_key = os.getenv('DEEPSEEK_API_KEY')
    
    # Generate English version
    markdown_en = generate_markdown(papers, lang='en')
    update_readme("README.md", markdown_en)
    
    # Generate Chinese version with translation
    markdown_zh = generate_markdown(papers, lang='zh')
    update_readme("README_CN.md", markdown_zh)
    
    save_papers_to_file(papers, lang='zh', api_key=api_key) 

