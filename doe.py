import pandas as pd
import streamlit as st


st.header('Design of experiment technique on *Candida sorboxylosa*')
st.write('Coffe is a crop of sifnificant socioeconomic importance, and the reuse of agri-food by-products and biowate has great potential across several industries. Coffe wastewater is a valuable resource containing esssential nutrinents that can be utilized by Candida sorboxylosa for a single-cell protein (SCP) production. This utilization contributes to mitigating the negative impacts of agro-industrial waste.')
st.write('The optiminzation of culture conditions using the design of experiments (DoE) technique is crucial in usderstanding the evironmental factors influencing metabolite production.')
st.write('In our study, the DoE thecnique was employed to analyze culture conditions, incluiding room temperatura, pH 8.4, aditation at 200 rpm, a headspace of 60% (v/v), and an inoculum of 0,75 optical density at 600 nm over 28-h period. This approach resulted in a remarkable SCP yield of 64.4% and dry cell weight of 2.26 g/L.')
st.write('It is noteworthy that there is no literature reporting SCP production under alkaline pH conditions in yeast. Intrerestingly, our work demonstrated that an alkaline pH of 8.4 significantly influenced SCP production by C. sorboxylosa. ')
st.write('The DoE technique proced to be an efficient statistical tool for optimizing culture conditions, offering several advantages, such as:')
st.subheader('Comparison DoE technique vs Literature:')
st.markdown("""
- (i) conducting cultures at room temperature to minimize unnecessart energy consumption;
- (ii) reducing the incybation time from 46 to 28 h , thereby enchancing overall productivity;
- (iii) achieving 1.7-fold increase in SCP yield compared to previous basal productuion levels.
""")

data1 = {
    'Temperature °C': 25,
    'pH': 8.4,
    'Agitation (rpm)': 200,
    'Headspace (%v/v)': 60,
    'Inoculo':0.75,
    'Optical Density (nm)': 600,
    'Incubation (h)': 28,
    'Yield (%)': 64.4,
    'Dry cell (g/L)': 2.26,
}

data2 = {
        'Temperature °C': 25,
        'pH': 'Acid',
        'Agitation (rpm)': 200,
        'Headspace (%v/v)': 60,
        'Inoculo':0.75,
        'Optical Density (nm)': 600,
        'Incubation (h)': 46,
        '---': '---',
        'Yield (%)': round(64.4/1.7,2),
        'Dry cell (g/L)': 'No data',
    }

data3 = {
        'Temperature °C': [25,'---'],
        'pH': [8.4, 'Acid'],
        'Agitation (rpm)': [200,'---'],
        'Headspace (%v/v)': [60,'---'],
        'Inoculo':[0.75,'---'],
        'Optical Density (nm)': [600,'---'],
        'Incubation (h)': [28,46],
        '---': '---',
        'Yield (%)': [64.4,round(64.4/1.7,2)],
        'Dry cell (g/L)': [2.26,'---'],
    }
df1 = pd.DataFrame(data1, index=['DoE technique'])
df2 = pd.DataFrame(data2, index=['Literatura'])
st.divider()
st.subheader('Data Analysis')

if st.button('Design of experiments (DoE) technique parameters and results'):
    st.dataframe(df1.transpose())

if st.toggle('DoE vs Literature'):
    st.write('From the information provided we can assume that the literature experiment introduces the same parameters as the experiment with the exception for the **pH** and **incubation period**, as such we can make a crude comparison:')
    df_combined = pd.concat([df1, df2], ignore_index=False)
    st.dataframe(df_combined.transpose())

    if st.button('Show graphs'):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Yield (%)')
            st.bar_chart(df_combined['Yield (%)'], y_label='Yield (%)')

            st.subheader('pH')
            st.bar_chart(df_combined['pH'], y_label='pH')

        with col2:
            st.subheader('Incubation (h)')
            st.bar_chart(df_combined['Incubation (h)'], y_label='pH')



if st.toggle('Add your own technique'):
    st.write('From the information provided we can assume that the literature experiment introduces the same parameters as the experiment with the exception for the **pH** and **incubation period**, as well as a 1.7 reduction on yield as such we can make a crude comparison:')
    with st.form("User Technique"):
        st.subheader("Enter the Parameters Below:")
    
    # Input fields for all parameters
        temperature = st.number_input("Temperature (°C)", value=25)
        ph = st.text_input("pH", value="8.4")
        agitation = st.number_input("Agitation (rpm)", value=200)
        headspace = st.number_input("Headspace (%v/v)", value=60)
        inoculo = st.number_input("Inoculo (v/v)", value=0.75)
        optical_density = st.number_input("Optical Density (nm)", value=600)
        incubation = st.number_input("Incubation (h)", value=48)
        yield_percentage = st.number_input("Yield (%)", value=64.4)
        dry_cell = st.number_input("Dry Cell (g/L)", value=2.26)

        # Submit button
        submitted = st.form_submit_button("Submit")

    if submitted:
        data3 = {
                'Temperature °C': temperature,
                'pH': ph,
                'Agitation (rpm)': agitation,
                'Headspace (%v/v)': headspace,
                'Inoculo': inoculo,
                'Optical Density (nm)': optical_density,
                'Incubation (h)': incubation,
                '---': '---',
                'Yield (%)': yield_percentage,
                'Dry cell (g/L)': dry_cell,
            }


        df3 = pd.DataFrame(data3, index=['User Input'])
        df_final = pd.concat([df1, df2, df3], ignore_index=False)
        st.dataframe(df_final.transpose())
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Yield (%)')
            st.bar_chart(df_final['Yield (%)'], y_label='Yield (%)')

            st.subheader('pH')
            st.bar_chart(df_final['pH'], y_label='pH')

        with col2:
            st.subheader('Incubation (h)')
            st.bar_chart(df_final['Incubation (h)'], y_label='pH')




