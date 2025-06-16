import streamlit as st
from PIL import Image

st.title('개인 블로그')
st.write('')

st.header('관심분야')
col_1, col_2= st.columns([1,1])

with col_1:
    st.subheader('대중교통')
    img1 = Image.open('img1.jpg')
    st.image(img1, width=300)

with col_2:
    st.subheader('산업안전')
    img2 = Image.open('img2.jpg')
    st.image(img2, width=300)
st.write('')

st.header('관심사항')
tab_1, tab_2, tab_3 = st.tabs(['대중교통 지역 불균형','성별','연령대'])

with tab_1:
    st.subheader('대중교통 지역 불균형')
    img3 = Image.open('img3.png')
    st.image(img3, width=600)
    st.caption('https://www.kotsa.or.kr/ptc/')
    st.markdown('**대중교통 지역별 접근성 편차 문제 해결**')
    st.markdown(' - 대중교통 이용층 대상별 특성 고려')
    st.markdown(' - 지역 교통 인프라 효과 분석')
    st.markdown(' - 교통약자 이동 경로 최적화')

with tab_2:
    st.subheader('EHS(Environment, Health, Safety)')
    st.markdown('**작업장, 커뮤니티 및 공공 장소와 같은 다양한 환경에서 인간의 건강과 환경을 보호하는 데 중점을 둔 종합적인 여러 전문 분야 영역**')
    st.markdown('**대중교통 지역별 접근성 편차 문제 해결**')
    st.markdown(' - 품질: FMEA, Fishbone Diagram → 안전사고 원인 분석')
    st.markdown(' - 공정개선: 위험 작업 공정 재설계, 자동화')
    st.markdown(' - 데이터 분석: 위험성 평가')
st.write('')

st.header('관심기업')
col_1, col_2= st.columns([1,1])

with col_1:
    st.subheader('코레일(한국철도공사)')
    img5 = Image.open('img5.jpg')
    st.image(img5, width=300)
    img4 = Image.open('img4.jpg')
    st.image(img4, width=300)
    st.markdown('**철도안전보건경영방침**')
    st.markdown(' - 안전역량 집중')
    st.markdown(' - 현장중심 안전관리')
    st.markdown(' - 위험관리 체계화')
    st.markdown(' - 철도안전 첨단화')

with col_2:
    st.subheader('세이프웨어')
    img6 = Image.open('img6.jpg')
    st.image(img6, width=300)
    st.markdown('**작업자 추락방지**')
    st.markdown(' - 작업자 추락감지 시스템')
    st.markdown(' - 웨어러블 기반 실시간 안전 모니터링')
    st.markdown(' - 위험관리 체계화')
