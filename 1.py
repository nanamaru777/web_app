import streamlit as st

st.title("経理担当必見！！　便利な Excel API を使ってみよう")
st.write("Microsoft Excelの機能をプログラムから操作するためのAPI（アプリケーションプログラミングインターフェース）です。これにより、開発者はプログラムやスクリプトを通じてExcelワークシートを操作し、データの入力、編集、解析、グラフの作成などを自動化することができます。")

st.write("実際にどのような使い方ができるかご紹介します！")

st.write("A1：法人名、B1：法人番号、C1：郵便番号、D1：所在地、E1：登録番号、F1：登録有無の見出しを入力します")

st.write("A2に法人名を手入力します")

st.write("B2に法人番号を取得する式を設定します")
st.write("=WEBSERVICE("https://api.excelapi.org/company/number?name="&ENCODEURL($A2))")
st.write("※取得されない場合は調べて手入力してください")

st.write("C2に郵便番号を取得する式を設定します")
st.write("=WEBSERVICE("https://api.excelapi.org/company/zipcode?id="&$B2)")

st.write("D2に郵便番号を取得する式を設定します")
st.write("=WEBSERVICE("https://api.excelapi.org/company/address?id="&$B2)")

st.write("E2にインボイス登録番号を取得する式を設定します")
st.write("=”T”＆B2")

st.write("F2にインボイス登録の有無を取得する式を設定します")
st.write("=WEBSERVICE("https://api.excelapi.org/company/invoice_check?id="&$E2)")

st.write("詳しくは、ExcelAPIの公式ドキュメントをご覧ください：[ExcelAPI公式ドキュメント](https://excelapi.org/docs/)")
