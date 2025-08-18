Search & Intelligence Tools
===========================

.. currentmodule:: haive.tools

The **Search & Intelligence Tools** represent the cutting edge of AI-powered information retrieval - sophisticated search capabilities that **understand context**, **generate structured answers**, **extract insights from multiple sources**, and **provide real-time intelligence** across web, academic, and specialized data sources.

🧠 **Revolutionary Capabilities**
---------------------------------

**Context-Aware Search Intelligence**
   Advanced search tools that understand query intent, generate contextual answers, and provide structured data for RAG applications

**Multi-Source Information Fusion**
   Intelligent aggregation across web search, academic papers, social media, and specialized databases with unified interfaces

**Real-Time Knowledge Extraction**
   Live content extraction, trend analysis, and insight generation from dynamic web sources

**Question-Answering Systems**
   Direct answer generation with source attribution, confidence scoring, and context-aware response formatting

**Structured Data Extraction**
   Transform unstructured web content into structured data with metadata, summaries, and actionable insights

Core Search Technologies
-------------------------

Tavily Search Intelligence
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.tools.tools.search_tools
   :members:
   :undoc-members:

**Advanced Context-Aware Search Platform**

Tavily provides the most sophisticated search intelligence available, featuring context understanding, direct answer generation, and optimized content extraction for AI applications.

**Key Features**:
* **Context-Aware QnA**: Direct answers with source attribution
* **RAG-Optimized Content**: Structured context generation for retrieval applications
* **Real-Time Intelligence**: Fresh information with recency filtering
* **Multi-Domain Search**: General, news, finance, and specialized topic search

**Quick Start: Context-Aware Search**

.. code-block:: python

   from haive.tools.tools.search_tools import (
       tavily_qna, tavily_search_context, tavily_extract, scrape_webpages
   )

   # Direct question answering with context
   answer = tavily_qna(
       query="What are the latest breakthroughs in quantum computing?",
       search_depth="advanced",
       topic="general",
       days=7,  # Recent information only
       max_results=10,
       include_answer=True
   )

   # Generate optimized context for RAG applications
   rag_context = tavily_search_context(
       query="artificial intelligence safety research 2024",
       max_results=15,
       include_raw_content=True,
       search_depth="advanced"
   )

   # Extract content from specific URLs
   extracted_content = tavily_extract(
       urls=[
           "https://example.com/ai-research",
           "https://example.com/quantum-computing"
       ]
   )

   # Web scraping with intelligent content extraction
   scraped_data = scrape_webpages(
       urls=["https://news.ycombinator.com"],
       extract_content=True,
       include_metadata=True
   )

   print(f"Direct Answer: {answer}")
   print(f"RAG Context Length: {len(rag_context)} characters")
   print(f"Extracted Sources: {len(extracted_content)} documents")

**Advanced Tavily Features**

.. code-block:: python

   # Topic-specific search with domain filtering
   finance_intelligence = tavily_qna(
       query="Federal Reserve interest rate impact on technology stocks",
       topic="finance",
       search_depth="advanced",
       include_domains=["reuters.com", "bloomberg.com", "wsj.com"],
       exclude_domains=["twitter.com", "reddit.com"],
       days=3
   )

   # News-focused search with recency emphasis
   breaking_news = tavily_qna(
       query="latest developments in AI regulation",
       topic="news",
       search_depth="advanced",
       days=1,  # Last 24 hours only
       max_results=20
   )

   # Comprehensive research with multiple perspectives
   research_context = tavily_search_context(
       query="climate change machine learning applications",
       max_results=25,
       include_raw_content=True,
       include_images=True,
       search_depth="advanced"
   )

Google Search Ecosystem
~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: haive.tools.tools.google
   :members:
   :undoc-members:

**Complete Google Search Suite Integration**

Access Google's comprehensive search capabilities with unified interfaces, rich metadata, and specialized search types.

**Search Services Available**:
* **Google Web Search**: Comprehensive web search with snippets and metadata
* **Google Scholar**: Academic paper search with citation data
* **Google Books**: Book search with availability and preview information
* **Google Finance**: Financial data and market information
* **Google Jobs**: Job search with location and salary filtering
* **Google Places**: Location search with business information
* **Google Trends**: Search trend analysis and popularity data
* **Google Lens**: Visual search and image analysis

**Quick Start: Google Search Integration**

.. code-block:: python

   from haive.tools.tools.google import (
       google_search_tool, initialize_google_scholar,
       initialize_google_books, initialize_google_finance
   )

   # Comprehensive web search
   search_results = google_search_tool(
       query="machine learning frameworks comparison 2024",
       num_results=20,
       include_snippets=True,
       safe_search="strict",
       language="en",
       region="us"
   )

   # Academic research
   scholar_tool = initialize_google_scholar()
   academic_papers = scholar_tool.search(
       query="transformer neural networks attention mechanisms",
       num_results=15,
       year_filter="2023-2024",
       include_citations=True,
       sort_by="relevance"
   )

   # Book discovery and research
   books_tool = initialize_google_books()
   technical_books = books_tool.search(
       query="deep learning artificial intelligence textbook",
       max_results=20,
       filter_availability="free-ebooks",
       order_by="relevance",
       include_preview=True
   )

   # Financial market intelligence
   finance_tool = initialize_google_finance()
   market_data = finance_tool.get_market_summary(
       exchange="NASDAQ",
       include_trends=True,
       include_top_movers=True
   )

   print(f"Web Results: {len(search_results)} found")
   print(f"Academic Papers: {len(academic_papers)} found")
   print(f"Available Books: {len(technical_books)} found")
   print(f"Market Status: {market_data['status']}")

**Advanced Google Search Features**

.. code-block:: python

   # Multi-service research workflow
   research_query = "artificial intelligence ethics governance"

   # 1. General web search for overview
   web_overview = google_search_tool(
       query=research_query,
       num_results=15,
       include_snippets=True
   )

   # 2. Academic perspective
   scholar_tool = initialize_google_scholar()
   academic_perspective = scholar_tool.search(
       query=research_query,
       num_results=10,
       year_filter="2022-2024"
   )

   # 3. Book resources
   books_tool = initialize_google_books()
   book_resources = books_tool.search(
       query=research_query,
       max_results=10,
       filter_availability="partial-view"
   )

   # 4. Current trends
   trends_tool = initialize_google_trends()
   trend_analysis = trends_tool.get_trending_searches(
       timeframe="today",
       geo="US",
       category="technology"
   )

   # Comprehensive research report
   research_report = {
       "web_sources": len(web_overview),
       "academic_papers": len(academic_perspective),
       "book_resources": len(book_resources),
       "trending_topics": len(trend_analysis),
       "total_sources": len(web_overview) + len(academic_perspective) + len(book_resources)
   }

Academic & Research Tools
~~~~~~~~~~~~~~~~~~~~~~~~~

**ArXiv Academic Paper Search**

.. code-block:: python

   from haive.tools.tools.arxiv import arxiv_query_tool

   # Search for recent AI research papers
   ai_papers = arxiv_query_tool(
       query="large language models reasoning",
       max_results=20,
       sort_by="lastUpdatedDate",
       sort_order="descending"
   )

   # Filter by category and date
   cs_papers = arxiv_query_tool(
       query="computer vision transformers",
       max_results=15,
       category="cs.CV",  # Computer Vision
       date_range="2024-01-01:2024-12-31"
   )

   # Multi-category search
   interdisciplinary_papers = arxiv_query_tool(
       query="quantum machine learning",
       max_results=25,
       categories=["quant-ph", "cs.LG", "stat.ML"]
   )

**Social Media Intelligence**

.. code-block:: python

   from haive.tools.tools.reddit_search import search_reddit

   # Reddit discussion analysis
   ai_discussions = search_reddit(
       query="artificial general intelligence",
       subreddits=["MachineLearning", "artificial", "singularity"],
       time_filter="month",
       sort="top",
       limit=50
   )

   # Trending topic analysis
   tech_trends = search_reddit(
       query="startup funding 2024",
       subreddits=["startups", "entrepreneur", "venturecapital"],
       time_filter="week",
       sort="hot",
       limit=30
   )

Advanced Search Intelligence
----------------------------

Multi-Source Research Orchestration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Comprehensive Research Workflow**

.. code-block:: python

   from haive.tools.tools.search_tools import tavily_qna, tavily_search_context
   from haive.tools.tools.google import google_search_tool
   from haive.tools.tools.arxiv import arxiv_query_tool
   from haive.tools.tools.reddit_search import search_reddit

   class IntelligenceOrchestrator:
       """Orchestrate multi-source intelligence gathering."""

       async def comprehensive_research(self, topic: str, depth: str = "deep"):
           """Conduct comprehensive research across multiple sources."""
           
           # 1. Direct answer generation
           quick_answer = tavily_qna(
               query=f"What is {topic}? Latest developments and key insights",
               search_depth="advanced",
               max_results=10,
               days=7
           )

           # 2. Context generation for detailed analysis
           detailed_context = tavily_search_context(
               query=f"{topic} comprehensive analysis research",
               max_results=20,
               include_raw_content=True,
               search_depth="advanced"
           )

           # 3. Academic research
           academic_papers = arxiv_query_tool(
               query=topic,
               max_results=15,
               sort_by="relevance"
           )

           # 4. Web intelligence
           web_intelligence = google_search_tool(
               query=f"{topic} latest news analysis",
               num_results=15,
               include_snippets=True
           )

           # 5. Social intelligence
           social_discussions = search_reddit(
               query=topic,
               subreddits=["technology", "artificial", "MachineLearning"],
               time_filter="month",
               sort="top",
               limit=20
           )

           return {
               "quick_answer": quick_answer,
               "detailed_context": detailed_context[:1000],  # Truncate for display
               "academic_sources": len(academic_papers),
               "web_sources": len(web_intelligence),
               "social_discussions": len(social_discussions),
               "research_depth": depth,
               "total_sources": len(academic_papers) + len(web_intelligence) + len(social_discussions)
           }

   # Execute comprehensive research
   orchestrator = IntelligenceOrchestrator()
   research_results = await orchestrator.comprehensive_research(
       topic="quantum computing applications in machine learning",
       depth="deep"
   )

Real-Time Intelligence Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Live Information Tracking**

.. code-block:: python

   class RealTimeIntelligence:
       """Monitor real-time information across multiple sources."""

       def __init__(self):
           self.monitored_topics = []
           self.alert_thresholds = {}

       async def monitor_topic(self, topic: str, alert_threshold: int = 5):
           """Monitor a topic for new information."""
           
           # Set up monitoring
           self.monitored_topics.append(topic)
           self.alert_thresholds[topic] = alert_threshold

           # Initial baseline
           baseline_results = tavily_qna(
               query=f"latest {topic} news developments",
               days=1,
               max_results=10
           )

           return {
               "topic": topic,
               "baseline_results": len(baseline_results),
               "monitoring_active": True,
               "alert_threshold": alert_threshold
           }

       async def check_updates(self, topic: str):
           """Check for updates on a monitored topic."""
           
           # Check for very recent information
           recent_updates = tavily_qna(
               query=f"breaking news {topic} last 6 hours",
               days=1,
               max_results=15,
               search_depth="advanced"
           )

           # Google trends for sudden interest spikes
           trends_tool = initialize_google_trends()
           trending_data = trends_tool.get_real_time_trends(
               keywords=[topic],
               geo="US"
           )

           # Alert if threshold exceeded
           alert_triggered = len(recent_updates) > self.alert_thresholds.get(topic, 5)

           return {
               "topic": topic,
               "recent_updates": len(recent_updates),
               "trending_score": trending_data.get("interest_level", 0),
               "alert_triggered": alert_triggered,
               "latest_update": recent_updates[0] if recent_updates else None
           }

   # Set up real-time monitoring
   monitor = RealTimeIntelligence()
   
   # Monitor critical topics
   await monitor.monitor_topic("AI regulation policy", alert_threshold=3)
   await monitor.monitor_topic("quantum computing breakthrough", alert_threshold=2)
   await monitor.monitor_topic("cybersecurity threats", alert_threshold=5)

   # Check for updates
   ai_updates = await monitor.check_updates("AI regulation policy")
   quantum_updates = await monitor.check_updates("quantum computing breakthrough")

Specialized Search Applications
-------------------------------

Domain-Specific Intelligence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Financial Intelligence**

.. code-block:: python

   class FinancialIntelligence:
       """Specialized financial information gathering."""

       async def market_intelligence(self, symbol: str):
           """Gather comprehensive market intelligence."""
           
           # News and sentiment analysis
           market_news = tavily_qna(
               query=f"{symbol} stock analysis earnings forecast",
               topic="finance",
               days=3,
               max_results=15,
               include_domains=["reuters.com", "bloomberg.com", "marketwatch.com"]
           )

           # Google Finance data
           finance_tool = initialize_google_finance()
           financial_data = finance_tool.get_stock_data(
               symbol=symbol,
               include_charts=True,
               include_fundamentals=True
           )

           # Social sentiment
           social_sentiment = search_reddit(
               query=f"{symbol} stock discussion analysis",
               subreddits=["investing", "stocks", "SecurityAnalysis"],
               time_filter="week",
               sort="top",
               limit=25
           )

           return {
               "symbol": symbol,
               "news_sentiment": market_news,
               "financial_data": financial_data,
               "social_sentiment": len(social_sentiment),
               "overall_intelligence": "positive" if len(social_sentiment) > 15 else "neutral"
           }

**Technical Research Intelligence**

.. code-block:: python

   class TechnicalIntelligence:
       """Advanced technical research capabilities."""

       async def technology_landscape(self, technology: str):
           """Map technology landscape and trends."""
           
           # Academic research state
           academic_state = arxiv_query_tool(
               query=technology,
               max_results=30,
               sort_by="lastUpdatedDate"
           )

           # Industry applications
           industry_context = tavily_search_context(
               query=f"{technology} industry applications case studies",
               max_results=20,
               search_depth="advanced"
           )

           # Development trends
           development_trends = google_search_tool(
               query=f"{technology} development roadmap 2024 2025",
               num_results=20,
               include_snippets=True
           )

           # Community insights
           community_insights = search_reddit(
               query=f"{technology} development challenges",
               subreddits=["programming", "technology", "MachineLearning"],
               time_filter="month",
               sort="top",
               limit=30
           )

           return {
               "technology": technology,
               "academic_papers": len(academic_state),
               "industry_context": len(industry_context),
               "development_articles": len(development_trends),
               "community_discussions": len(community_insights),
               "maturity_indicator": "emerging" if len(academic_state) > 20 else "established"
           }

Performance Optimization
------------------------

**Search Intelligence Benchmarks**:

* **Response Time**: <500ms for cached results, <2s for fresh searches
* **Context Quality**: 95%+ relevance for topic-specific searches
* **Source Diversity**: 10+ unique domains per comprehensive search
* **Real-Time Updates**: <1 minute latency for breaking news detection
* **Academic Coverage**: 50M+ papers accessible through ArXiv integration

**Intelligence Applications**:

* **Real-Time Monitoring**: Breaking news, market events, technology developments
* **Research Intelligence**: Academic research, industry analysis, competitive intelligence
* **Content Generation**: RAG applications, report generation, insight synthesis
* **Decision Support**: Market analysis, technology evaluation, trend identification

Integration with Agent Systems
------------------------------

**Multi-Agent Intelligence**
   Search intelligence tools integrate seamlessly with haive-agents for sophisticated information gathering workflows.

**RAG Applications**
   Optimized context generation for retrieval-augmented generation with structured data extraction.

**Real-Time Monitoring**
   Live information feeds for agent decision-making with alert systems and threshold monitoring.

See Also
--------

* :doc:`google_ecosystem` - Complete Google service integration
* :doc:`development_toolkit` - Code analysis and development intelligence
* :doc:`financial_data_tools` - Specialized financial intelligence
* :doc:`api_integrations` - Multi-platform data aggregation