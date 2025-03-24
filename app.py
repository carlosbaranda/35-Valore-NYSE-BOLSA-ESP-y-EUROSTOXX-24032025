
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="App Bolsa", layout="wide")
st.title("App Bolsa - 140 valores de NYSE, España, EuroStoxx y ETFs")

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'JPM', 'WMT', 'UNH', 'KO', 'PEP', 'V', 'BAC', 'HD', 'DIS', 'MA', 'PYPL', 'INTC', 'IBM', 'CSCO', 'ORCL', 'NFLX', 'T', 'CVX', 'PFE', 'XOM', 'C', 'MCD', 'BA', 'ABT', 'CRM', 'MRK', 'QCOM', 'NKE', 'SAN.MC', 'BBVA.MC', 'ITX.MC', 'IBE.MC', 'REP.MC', 'AMS.MC', 'ANA.MC', 'CABK.MC', 'CLNX.MC', 'ENG.MC', 'FER.MC', 'GRF.MC', 'IAG.MC', 'MAP.MC', 'TEF.MC', 'ACX.MC', 'AENA.MC', 'ALM.MC', 'BKT.MC', 'COL.MC', 'ELE.MC', 'ENC.MC', 'EQT.MC', 'FCC.MC', 'LOG.MC', 'MEL.MC', 'NTGY.MC', 'PHM.MC', 'RED.MC', 'R4.MC', 'SAB.MC', 'SGRE.MC', 'SPS.MC', 'VIS.MC', 'ZOT.MC', 'AIR.PA', 'ADS.DE', 'ALV.DE', 'BN.PA', 'ENEL.MI', 'ENGI.PA', 'OR.PA', 'SAP.DE', 'SIE.DE', 'SU.PA', 'TTE.PA', 'VOW3.DE', 'DTE.DE', 'DPW.DE', 'BAS.DE', 'BAYN.DE', 'BMW.DE', 'CRH.L', 'DAI.DE', 'KER.PA', 'LVMH.PA', 'MC.PA', 'MT.AS', 'PHIA.AS', 'RWE.DE', 'SGO.PA', 'URW.AS', 'ZAL.DE', 'ATCO-A.ST', 'HEIA.AS', 'IFX.DE', 'LIN.DE', 'UCG.MI', 'STLA.MI', 'ENI.MI', 'SPY', 'QQQ', 'DIA', 'VTI', 'IWM', 'EFA', 'EEM', 'VNQ', 'LQD', 'HYG', 'XLF', 'XLK', 'XLE', 'XLY', 'XLV', 'XLI', 'XLB', 'XLC', 'XLRE', 'ARKK', 'ARKW', 'ARKF', 'ARKG', 'ARKQ', 'ARKX', 'SOXX', 'SMH', 'IBB', 'VHT', 'IYZ', 'XRT', 'XHB', 'XME', 'ITA', 'IYT']

@st.cache_data(ttl=3600)
def obtener_datos(tickers):
    data = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="90d")
            info = stock.info
            if len(hist) >= 7:
                hoy = (hist["Close"][-1] - hist["Open"][-1]) / hist["Open"][-1] * 100
                semana = (hist["Close"][-1] - hist["Close"][-6]) / hist["Close"][-6] * 100
                ytd = (hist["Close"][-1] - hist["Close"][0]) / hist["Close"][0] * 100
                mercado = mercado_dict.get(ticker, "Desconocido")
                data.append({
                    "Ticker": ticker,
                    "Nombre": info.get("shortName", ""),
                    "Mercado": mercado,
                    "Cambio Día (%)": round(hoy, 2),
                    "Cambio Semana (%)": round(semana, 2),
                    "Cambio YTD (%)": round(ytd, 2)
                })
        except:
            continue
    return pd.DataFrame(data)

mercado_dict = {
    "AAPL": "NYSE",
    "MSFT": "NYSE",
    "GOOGL": "NYSE",
    "AMZN": "NYSE",
    "TSLA": "NYSE",
    "META": "NYSE",
    "NVDA": "NYSE",
    "JPM": "NYSE",
    "WMT": "NYSE",
    "UNH": "NYSE",
    "KO": "NYSE",
    "PEP": "NYSE",
    "V": "NYSE",
    "BAC": "NYSE",
    "HD": "NYSE",
    "DIS": "NYSE",
    "MA": "NYSE",
    "PYPL": "NYSE",
    "INTC": "NYSE",
    "IBM": "NYSE",
    "CSCO": "NYSE",
    "ORCL": "NYSE",
    "NFLX": "NYSE",
    "T": "NYSE",
    "CVX": "NYSE",
    "PFE": "NYSE",
    "XOM": "NYSE",
    "C": "NYSE",
    "MCD": "NYSE",
    "BA": "NYSE",
    "ABT": "NYSE",
    "CRM": "NYSE",
    "MRK": "NYSE",
    "QCOM": "NYSE",
    "NKE": "NYSE",
    "SAN.MC": "España",
    "BBVA.MC": "España",
    "ITX.MC": "España",
    "IBE.MC": "España",
    "REP.MC": "España",
    "AMS.MC": "España",
    "ANA.MC": "España",
    "CABK.MC": "España",
    "CLNX.MC": "España",
    "ENG.MC": "España",
    "FER.MC": "España",
    "GRF.MC": "España",
    "IAG.MC": "España",
    "MAP.MC": "España",
    "TEF.MC": "España",
    "ACX.MC": "España",
    "AENA.MC": "España",
    "ALM.MC": "España",
    "BKT.MC": "España",
    "COL.MC": "España",
    "ELE.MC": "España",
    "ENC.MC": "España",
    "EQT.MC": "España",
    "FCC.MC": "España",
    "LOG.MC": "España",
    "MEL.MC": "España",
    "NTGY.MC": "España",
    "PHM.MC": "España",
    "RED.MC": "España",
    "R4.MC": "España",
    "SAB.MC": "España",
    "SGRE.MC": "España",
    "SPS.MC": "España",
    "VIS.MC": "España",
    "ZOT.MC": "España",
    "AIR.PA": "EuroStoxx",
    "ADS.DE": "EuroStoxx",
    "ALV.DE": "EuroStoxx",
    "BN.PA": "EuroStoxx",
    "ENEL.MI": "EuroStoxx",
    "ENGI.PA": "EuroStoxx",
    "OR.PA": "EuroStoxx",
    "SAP.DE": "EuroStoxx",
    "SIE.DE": "EuroStoxx",
    "SU.PA": "EuroStoxx",
    "TTE.PA": "EuroStoxx",
    "VOW3.DE": "EuroStoxx",
    "DTE.DE": "EuroStoxx",
    "DPW.DE": "EuroStoxx",
    "BAS.DE": "EuroStoxx",
    "BAYN.DE": "EuroStoxx",
    "BMW.DE": "EuroStoxx",
    "CRH.L": "EuroStoxx",
    "DAI.DE": "EuroStoxx",
    "KER.PA": "EuroStoxx",
    "LVMH.PA": "EuroStoxx",
    "MC.PA": "EuroStoxx",
    "MT.AS": "EuroStoxx",
    "PHIA.AS": "EuroStoxx",
    "RWE.DE": "EuroStoxx",
    "SGO.PA": "EuroStoxx",
    "URW.AS": "EuroStoxx",
    "ZAL.DE": "EuroStoxx",
    "ATCO-A.ST": "EuroStoxx",
    "HEIA.AS": "EuroStoxx",
    "IFX.DE": "EuroStoxx",
    "LIN.DE": "EuroStoxx",
    "UCG.MI": "EuroStoxx",
    "STLA.MI": "EuroStoxx",
    "ENI.MI": "EuroStoxx",
    "SPY": "ETF",
    "QQQ": "ETF",
    "DIA": "ETF",
    "VTI": "ETF",
    "IWM": "ETF",
    "EFA": "ETF",
    "EEM": "ETF",
    "VNQ": "ETF",
    "LQD": "ETF",
    "HYG": "ETF",
    "XLF": "ETF",
    "XLK": "ETF",
    "XLE": "ETF",
    "XLY": "ETF",
    "XLV": "ETF",
    "XLI": "ETF",
    "XLB": "ETF",
    "XLC": "ETF",
    "XLRE": "ETF",
    "ARKK": "ETF",
    "ARKW": "ETF",
    "ARKF": "ETF",
    "ARKG": "ETF",
    "ARKQ": "ETF",
    "ARKX": "ETF",
    "SOXX": "ETF",
    "SMH": "ETF",
    "IBB": "ETF",
    "VHT": "ETF",
    "IYZ": "ETF",
    "XRT": "ETF",
    "XHB": "ETF",
    "XME": "ETF",
    "ITA": "ETF",
    "IYT": "ETF",
}

df = obtener_datos(tickers)


st.subheader("🔎 Filtro por mercado")
mercado_seleccionado = st.selectbox("Selecciona un mercado:", ["Todos"] + sorted(df["Mercado"].unique()), key="filtro_mercado")
if mercado_seleccionado != "Todos":
    df = df[df["Mercado"] == mercado_seleccionado]


if not df.empty:
    st.subheader("📈 Datos Generales")
    st.dataframe(df, use_container_width=True)

# --- Gráfico por ticker con medias móviles y volumen ---

st.subheader("🔎 Filtro por mercado")
mercado_seleccionado = st.selectbox("Selecciona un mercado:", ["Todos"] + sorted(df["Mercado"].unique()), key="filtro_mercado")
if mercado_seleccionado != "Todos":
    df = df[df["Mercado"] == mercado_seleccionado]


if not df.empty:
    st.subheader("📊 Evolución del precio con medias móviles y volumen")
    seleccion = st.selectbox("Selecciona un ticker:", df["Ticker"])
    if seleccion:
        hist = yf.Ticker(seleccion).history(period="1y")
        hist["Media 50"] = hist["Close"].rolling(50).mean()
        hist["Media 200"] = hist["Close"].rolling(200).mean()

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True, gridspec_kw={'height_ratios': [2, 1]})
        hist[["Close", "Media 50", "Media 200"]].dropna().plot(ax=ax1)
        ax1.set_ylabel("Precio")
        ax1.set_title(f"Evolución de {seleccion}")

        hist["Volume"].plot(kind="bar", ax=ax2, color="gray")
        ax2.set_ylabel("Volumen")
        ax2.set_xlabel("Fecha")

        st.pyplot(fig)
