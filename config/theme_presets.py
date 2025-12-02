"""
CENTRALIZED APPLICATION CONFIGURATION
======================================
Single source of truth for app branding, naming, and configuration.
"""

APP_NAME = "ATLAS FINANCIAL INTELLIGENCE"
APP_NAME_SHORT = "Atlas Engine"
APP_TAGLINE = "Professional-Grade Financial Analysis & Valuation Engine"
APP_VERSION = "2.0.0"
COMPANY_NAME = "Atlas Financial Intelligence"

APP_ICON = "⚡"
AI_ICON = "🤖"
CHART_ICON = "📊"
REPORT_ICON = "📄"

PRIMARY_COLOR = "#1e88e5"
SECONDARY_COLOR = "#ffd700"
ACCENT_COLOR = "#64b5f6"
BACKGROUND_DARK = "#0a1929"
TEXT_PRIMARY = "#e3f2fd"
TEXT_SECONDARY = "#90caf9"

FEATURES = {
    'ai_chat': True,
    'live_dcf': True,
    'pdf_export': True,
    'investment_summary': True,
    'validation_engine': True,
    'quant_analysis': True,
    'forensic_accounting': True,
    'advanced_options': True,
}

DATA_SOURCES = {
    'primary': 'SEC EDGAR',
    'secondary': 'Yahoo Finance',
    'news': 'Google News RSS',
    'options': 'Yahoo Finance Options Chain',
}

AI_CONFIG = {
    'primary_model': 'gemini-2.0-flash-exp',
    'fallback_model': 'ollama/llama3.1',
    'temperature': 0.3,
    'max_tokens': 2000,
}

RATE_LIMITS = {
    'sec_edgar': 10,
    'yfinance': 2000,
    'ai_requests': 60,
}

DIRECTORIES = {
    'logs': 'logs',
    'saved_scenarios': 'saved_scenarios',
    'exports': 'exports',
    'cache': '.cache',
}

UI_CONFIG = {
    'page_title': f"{APP_ICON} {APP_NAME}",
    'page_icon': APP_ICON,
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
}

DISCLAIMERS = {
    'main': "This tool is for educational purposes only. Not financial advice.",
}

def get_app_title() -> str:
    return f"{APP_ICON} {APP_NAME}"

def get_app_header() -> str:
    return f"<div class='main-header'><h1>{APP_ICON} {APP_NAME}</h1><p>{APP_TAGLINE}</p></div>"

def get_footer() -> str:
    return f"<div class='footer'><p>{APP_NAME} v{APP_VERSION}</p></div>"

def is_feature_enabled(feature_name: str) -> bool:
    return FEATURES.get(feature_name, False)
