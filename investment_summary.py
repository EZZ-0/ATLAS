"""
INVESTMENT SUMMARY MODULE
=========================
One-page investment decision sheet with:
- Bull/Bear case generator
- Key metrics dashboard
- Risk assessment heatmap
- Valuation range
- Red flags detection

Professional design matching blue corporate theme.
"""

import streamlit as st
import pandas as pd
from typing import Dict, Any, List


class InvestmentSummaryGenerator:
    """
    Generates intelligent investment summaries based on financial data.
    Automatically creates bull/bear cases, risk assessments, and red flags.
    """
    
    def __init__(self, financials: Dict[str, Any]):
        """
        Initialize with financial data dictionary.
        
        Args:
            financials: Dict containing 'ticker', 'company_name', 'ratios', 
                       'growth_rates', 'income_statement', 'balance_sheet', 'market_data'
        """
        self.financials = financials
        self.ticker = financials.get('ticker', 'N/A')
        self.company_name = financials.get('company_name', 'Unknown Company')
        self.ratios = financials.get('ratios', pd.DataFrame())
        self.growth_rates = financials.get('growth_rates', {})
        self.market_data = financials.get('market_data', {})
    
    def _get_ratio(self, name: str, default: float = None) -> float:
        """Safely get a ratio value from the ratios DataFrame."""
        try:
            if self.ratios is None or self.ratios.empty:
                return default
            
            # Handle both row and column oriented DataFrames
            if name in self.ratios.index:
                val = self.ratios.loc[name]
                if isinstance(val, pd.Series):
                    val = val.iloc[0] if len(val) > 0 else default
                return float(val) if pd.notna(val) else default
            elif name in self.ratios.columns:
                val = self.ratios[name].iloc[0] if len(self.ratios) > 0 else default
                return float(val) if pd.notna(val) else default
            return default
        except:
            return default
    
    def _get_growth_rate(self, name: str, default: float = None) -> float:
        """Safely get a growth rate value."""
        try:
            val = self.growth_rates.get(name, default)
            return float(val) if val is not None and pd.notna(val) else default
        except:
            return default
    
    def generate_bull_case(self) -> List[str]:
        """
        Generate 3 bull case points based on positive financial signals.
        
        Returns:
            List of 3 bull case strings
        """
        bull_points = []
        
        # Check ROE
        roe = self._get_ratio('ROE')
        if roe is not None and roe > 0.15:
            bull_points.append(f"Strong profitability: ROE of {roe*100:.1f}%, indicating efficient use of shareholder capital")
        
        # Check Gross Margin
        gross_margin = self._get_ratio('Gross_Margin')
        if gross_margin is not None and gross_margin > 0.30:
            bull_points.append(f"Healthy margins: Gross margin of {gross_margin*100:.1f}%, demonstrating pricing power")
        
        # Check Operating Margin
        op_margin = self._get_ratio('Operating_Margin')
        if op_margin is not None and op_margin > 0.15:
            bull_points.append(f"Strong operating efficiency: Operating margin of {op_margin*100:.1f}%")
        
        # Check Current Ratio (liquidity)
        current_ratio = self._get_ratio('Current_Ratio')
        if current_ratio is not None and current_ratio > 1.5:
            bull_points.append(f"Solid liquidity: Current ratio of {current_ratio:.2f}x provides financial flexibility")
        
        # Check Debt/Equity (low leverage)
        de_ratio = self._get_ratio('Debt_to_Equity')
        if de_ratio is not None and de_ratio < 0.5:
            bull_points.append(f"Conservative balance sheet: Debt/Equity of {de_ratio:.2f}x indicates low financial risk")
        
        # Check Revenue Growth
        rev_cagr = self._get_growth_rate('Total_Revenue_CAGR')
        if rev_cagr is not None and rev_cagr > 0.10:
            bull_points.append(f"Consistent growth: Revenue CAGR of {rev_cagr*100:.1f}% demonstrates market expansion")
        
        # Check Cash Flow
        net_income = self._get_ratio('Net_Income')
        ocf = self._get_ratio('Operating_Cash_Flow')
        if net_income is not None and ocf is not None and ocf > net_income and net_income > 0:
            bull_points.append("Excellent cash generation: Operating cash flow exceeds net income")
        
        # Ensure we have exactly 3 points
        fallback_points = [
            "Established market position with brand recognition",
            "Diversified revenue streams reduce concentration risk",
            "Experienced management team with track record"
        ]
        
        while len(bull_points) < 3:
            for fallback in fallback_points:
                if fallback not in bull_points and len(bull_points) < 3:
                    bull_points.append(fallback)
        
        return bull_points[:3]
    
    def generate_bear_case(self) -> List[str]:
        """
        Generate 3 bear case points based on negative financial signals.
        
        Returns:
            List of 3 bear case strings
        """
        bear_points = []
        
        # Check P/E (high valuation)
        pe_ratio = self._get_ratio('PE_Ratio')
        if pe_ratio is not None and pe_ratio > 30:
            bear_points.append(f"Premium valuation: P/E ratio of {pe_ratio:.1f}x may limit upside potential")
        
        # Check Debt/Equity (high leverage)
        de_ratio = self._get_ratio('Debt_to_Equity')
        if de_ratio is not None and de_ratio > 1.5:
            bear_points.append(f"High leverage risk: Debt/Equity of {de_ratio:.2f}x increases financial vulnerability")
        
        # Check Revenue Growth (slow)
        rev_cagr = self._get_growth_rate('Total_Revenue_CAGR')
        if rev_cagr is not None and rev_cagr < 0.03:
            if rev_cagr < 0:
                bear_points.append(f"Revenue decline: {rev_cagr*100:.1f}% CAGR signals market share loss")
            else:
                bear_points.append(f"Slowing growth: {rev_cagr*100:.1f}% revenue CAGR suggests market maturation")
        
        # Check Operating Margin (thin)
        op_margin = self._get_ratio('Operating_Margin')
        if op_margin is not None and op_margin < 0.05:
            bear_points.append(f"Thin margins: Operating margin of {op_margin*100:.1f}% leaves little room for error")
        
        # Check Current Ratio (liquidity concerns)
        current_ratio = self._get_ratio('Current_Ratio')
        if current_ratio is not None and current_ratio < 1.0:
            bear_points.append(f"Liquidity concerns: Current ratio of {current_ratio:.2f}x may strain operations")
        
        # Check ROE (negative or low)
        roe = self._get_ratio('ROE')
        if roe is not None and roe < 0.05:
            if roe < 0:
                bear_points.append(f"Negative profitability: ROE of {roe*100:.1f}% indicates losses")
            else:
                bear_points.append(f"Low returns: ROE of {roe*100:.1f}% underperforms cost of equity")
        
        # Ensure we have exactly 3 points
        fallback_points = [
            "Competitive pressure may compress margins over time",
            "Macroeconomic sensitivity could impact near-term results",
            "Execution risk in strategic initiatives"
        ]
        
        while len(bear_points) < 3:
            for fallback in fallback_points:
                if fallback not in bear_points and len(bear_points) < 3:
                    bear_points.append(fallback)
        
        return bear_points[:3]
    
    def assess_risks(self) -> Dict[str, str]:
        """
        Assess risk levels across 5 categories.
        
        Returns:
            Dict with risk categories and levels (LOW, MODERATE, HIGH)
        """
        risks = {}
        
        # Financial Health: Based on Current Ratio + Debt/Equity
        current_ratio = self._get_ratio('Current_Ratio', 1.0)
        de_ratio = self._get_ratio('Debt_to_Equity', 1.0)
        
        if current_ratio >= 1.5 and de_ratio <= 0.5:
            risks['Financial Health'] = 'LOW'
        elif current_ratio < 1.0 or de_ratio > 2.0:
            risks['Financial Health'] = 'HIGH'
        else:
            risks['Financial Health'] = 'MODERATE'
        
        # Valuation: Based on P/E ratio
        pe_ratio = self._get_ratio('PE_Ratio', 20.0)
        
        if pe_ratio is not None:
            if pe_ratio < 20:
                risks['Valuation'] = 'LOW'
            elif pe_ratio > 40:
                risks['Valuation'] = 'HIGH'
            else:
                risks['Valuation'] = 'MODERATE'
        else:
            risks['Valuation'] = 'MODERATE'
        
        # Growth: Based on Revenue CAGR
        rev_cagr = self._get_growth_rate('Total_Revenue_CAGR', 0.05)
        
        if rev_cagr is not None:
            if rev_cagr > 0.10:
                risks['Growth'] = 'LOW'
            elif rev_cagr < 0:
                risks['Growth'] = 'HIGH'
            else:
                risks['Growth'] = 'MODERATE'
        else:
            risks['Growth'] = 'MODERATE'
        
        # Liquidity: Based on Current Ratio
        if current_ratio >= 2.0:
            risks['Liquidity'] = 'LOW'
        elif current_ratio < 1.0:
            risks['Liquidity'] = 'HIGH'
        else:
            risks['Liquidity'] = 'MODERATE'
        
        # Profitability: Based on ROE + Operating Margin
        roe = self._get_ratio('ROE', 0.10)
        op_margin = self._get_ratio('Operating_Margin', 0.10)
        
        if roe is not None and op_margin is not None:
            if roe > 0.15 and op_margin > 0.15:
                risks['Profitability'] = 'LOW'
            elif roe < 0 or op_margin < 0.05:
                risks['Profitability'] = 'HIGH'
            else:
                risks['Profitability'] = 'MODERATE'
        else:
            risks['Profitability'] = 'MODERATE'
        
        return risks
    
    def detect_red_flags(self) -> List[str]:
        """
        Detect major red flags in the financial data.
        
        Returns:
            List of red flag warnings, or success message if none
        """
        red_flags = []
        
        # Negative ROE
        roe = self._get_ratio('ROE')
        if roe is not None and roe < 0:
            red_flags.append(f"Negative return on equity ({roe*100:.1f}%) - company is destroying shareholder value")
        
        # High Debt/Equity
        de_ratio = self._get_ratio('Debt_to_Equity')
        if de_ratio is not None and de_ratio > 2.0:
            red_flags.append(f"High leverage ({de_ratio:.2f}x D/E) - elevated bankruptcy risk")
        
        # Liquidity Crisis
        current_ratio = self._get_ratio('Current_Ratio')
        if current_ratio is not None and current_ratio < 0.8:
            red_flags.append(f"Liquidity crisis (Current Ratio: {current_ratio:.2f}x) - may struggle to meet obligations")
        
        # Revenue Decline
        rev_cagr = self._get_growth_rate('Total_Revenue_CAGR')
        if rev_cagr is not None and rev_cagr < -0.05:
            red_flags.append(f"Significant revenue decline ({rev_cagr*100:.1f}% CAGR) - business is shrinking")
        
        # Extreme Valuation
        pe_ratio = self._get_ratio('PE_Ratio')
        if pe_ratio is not None and pe_ratio > 100:
            red_flags.append(f"Extreme valuation (P/E: {pe_ratio:.1f}x) - priced for perfection")
        
        # If no red flags, return positive message
        if not red_flags:
            red_flags.append("✅ No major red flags detected - fundamentals appear healthy")
        
        return red_flags
    
    def calculate_valuation_range(self) -> Dict[str, float]:
        """
        Calculate bear/base/bull valuation scenarios.
        
        Returns:
            Dict with bear_case, base_case, bull_case prices
        """
        current_price = self._get_ratio('Current_Price')
        
        # Handle missing or invalid price
        if current_price is None or current_price <= 0:
            return {
                'bear_case': 0,
                'base_case': 0,
                'bull_case': 0,
                'bear_pct': -20,
                'bull_pct': 25
            }
        
        return {
            'bear_case': current_price * 0.80,  # -20%
            'base_case': current_price,
            'bull_case': current_price * 1.25,  # +25%
            'bear_pct': -20,
            'bull_pct': 25
        }
    
    def get_key_metrics(self) -> Dict[str, Any]:
        """
        Get key metrics for display.
        
        Returns:
            Dict of metric names to values
        """
        return {
            'Current Price': self._get_ratio('Current_Price'),
            'P/E Ratio': self._get_ratio('PE_Ratio'),
            'Market Cap': self._get_ratio('Market_Cap'),
            'Revenue': self._get_ratio('Total_Revenue'),
            'Net Income': self._get_ratio('Net_Income'),
            'ROE': self._get_ratio('ROE'),
            'Debt/Equity': self._get_ratio('Debt_to_Equity'),
            'Current Ratio': self._get_ratio('Current_Ratio')
        }


def render_investment_summary_tab(ticker: str, financials: Dict[str, Any]):
    """
    Render the Investment Summary tab with all components.
    
    Args:
        ticker: Company ticker symbol
        financials: Financial data dictionary
    """
    
    # Header with gradient
    st.markdown("""
    <style>
    .summary-header {
        background: linear-gradient(135deg, #1e88e5 0%, #42a5f5 100%);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: white;
        text-align: center;
    }
    .bull-card {
        background: linear-gradient(135deg, #2e7d32 0%, #4caf50 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        height: 100%;
    }
    .bear-card {
        background: linear-gradient(135deg, #c62828 0%, #f44336 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        height: 100%;
    }
    .metric-card {
        background: linear-gradient(135deg, #1565c0 0%, #1976d2 100%);
        padding: 15px;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 5px 0;
    }
    .risk-low { color: #4caf50; font-weight: bold; }
    .risk-moderate { color: #ff9800; font-weight: bold; }
    .risk-high { color: #f44336; font-weight: bold; }
    .valuation-card {
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin: 5px;
    }
    .val-bear { background-color: #ffebee; border: 2px solid #f44336; }
    .val-base { background-color: #e3f2fd; border: 2px solid #1976d2; }
    .val-bull { background-color: #e8f5e9; border: 2px solid #4caf50; }
    .red-flag-item {
        background-color: #fff3e0;
        padding: 10px;
        border-left: 4px solid #ff9800;
        margin: 5px 0;
        border-radius: 0 5px 5px 0;
    }
    .green-flag-item {
        background-color: #e8f5e9;
        padding: 10px;
        border-left: 4px solid #4caf50;
        margin: 5px 0;
        border-radius: 0 5px 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if not financials:
        st.warning("Please extract company data first to view the Investment Summary.")
        return
    
    # Initialize generator
    generator = InvestmentSummaryGenerator(financials)
    company_name = financials.get('company_name', ticker)
    
    # Header
    st.markdown(f"""
    <div class="summary-header">
        <h2>Investment Summary</h2>
        <h3>{ticker} - {company_name}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Bull/Bear Cases - Side by Side
    col1, col2 = st.columns(2)
    
    with col1:
        bull_case = generator.generate_bull_case()
        st.markdown("""
        <div class="bull-card">
            <h4>Bull Case</h4>
        </div>
        """, unsafe_allow_html=True)
        for point in bull_case:
            st.markdown(f"• {point}")
    
    with col2:
        bear_case = generator.generate_bear_case()
        st.markdown("""
        <div class="bear-card">
            <h4>Bear Case</h4>
        </div>
        """, unsafe_allow_html=True)
        for point in bear_case:
            st.markdown(f"• {point}")
    
    st.markdown("---")
    
    # Key Metrics
    st.markdown("### Key Metrics")
    metrics = generator.get_key_metrics()
    
    cols = st.columns(4)
    metric_items = list(metrics.items())
    
    for i, (name, value) in enumerate(metric_items):
        with cols[i % 4]:
            if value is not None:
                if name in ['Current Price']:
                    display_val = f"${value:,.2f}"
                elif name in ['Market Cap', 'Revenue', 'Net Income']:
                    if abs(value) >= 1e9:
                        display_val = f"${value/1e9:,.1f}B"
                    elif abs(value) >= 1e6:
                        display_val = f"${value/1e6:,.1f}M"
                    else:
                        display_val = f"${value:,.0f}"
                elif name in ['ROE']:
                    display_val = f"{value*100:.1f}%"
                elif name in ['P/E Ratio', 'Debt/Equity', 'Current Ratio']:
                    display_val = f"{value:.2f}x"
                else:
                    display_val = f"{value:,.2f}"
            else:
                display_val = "N/A"
            
            st.metric(label=name, value=display_val)
    
    st.markdown("---")
    
    # Risk Assessment
    st.markdown("### Risk Assessment")
    risks = generator.assess_risks()
    
    risk_cols = st.columns(5)
    risk_items = list(risks.items())
    
    for i, (category, level) in enumerate(risk_items):
        with risk_cols[i]:
            if level == 'LOW':
                color = "🟢"
                css_class = "risk-low"
            elif level == 'HIGH':
                color = "🔴"
                css_class = "risk-high"
            else:
                color = "🟡"
                css_class = "risk-moderate"
            
            st.markdown(f"""
            <div style="text-align: center; padding: 10px; background: #f5f5f5; border-radius: 8px;">
                <div style="font-size: 24px;">{color}</div>
                <div style="font-weight: bold;">{category}</div>
                <div class="{css_class}">{level}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Valuation Range
    st.markdown("### Valuation Range")
    valuation = generator.calculate_valuation_range()
    
    val_cols = st.columns(3)
    
    with val_cols[0]:
        st.markdown(f"""
        <div class="valuation-card val-bear">
            <div style="font-weight: bold; color: #c62828;">Bear Case</div>
            <div style="font-size: 24px; font-weight: bold; color: #c62828;">${valuation['bear_case']:,.2f}</div>
            <div style="color: #c62828;">({valuation['bear_pct']}%)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with val_cols[1]:
        st.markdown(f"""
        <div class="valuation-card val-base">
            <div style="font-weight: bold; color: #1565c0;">Base Case</div>
            <div style="font-size: 24px; font-weight: bold; color: #1565c0;">${valuation['base_case']:,.2f}</div>
            <div style="color: #1565c0;">(Current)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with val_cols[2]:
        st.markdown(f"""
        <div class="valuation-card val-bull">
            <div style="font-weight: bold; color: #2e7d32;">Bull Case</div>
            <div style="font-size: 24px; font-weight: bold; color: #2e7d32;">${valuation['bull_case']:,.2f}</div>
            <div style="color: #2e7d32;">(+{valuation['bull_pct']}%)</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Red Flags
    st.markdown("### Red Flags & Concerns")
    red_flags = generator.detect_red_flags()
    
    for flag in red_flags:
        if flag.startswith("✅"):
            st.markdown(f"""
            <div class="green-flag-item">
                {flag}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="red-flag-item">
                ⚠️ {flag}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("Investment Summary generated automatically based on financial data. This is not investment advice.")

