import streamlit as st

st.title('Vorhersage der deutschen CO2-Emissionen')

"Autor: Dimitri Bennhäuser (https://github.com/dimitribenn)"

from scipy.stats import linregress
st.subheader("Vorhersage")

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
emissions_per_year = [10.3, 10.0, 10.1, 10.2, 9.7, 9.7, 9.7, 9.5, 9.1, 8.5, 7.7]

regression_result = linregress(years, emissions_per_year)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept

def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result

desired_year = st.number_input('Jahr', value=2022)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

"Die Vorhersage der Emissione für das ausgewählte Jahr ist:"

st.write(prediction_rounded)

"Tonnen pro Kopf pro Jahr"

st.subheader("Über das Modell und die Daten")

"Das Modell ist ein lineares Regressionsmodell auf Grundlage von 2010 bis 2020. "
"Es steht ein Datenpunkt pro Jahr zur Verfügung."

"Die Daten stammen aus folgenden Quellen:"

"- Global Carbon Project. (2021). Supplemental data of Global Carbon Project 2021 (1.0) [Data set]. " \
"Global Carbon Project. https://doi.org/10.18160/gcp-2021. "
"- Andrew, Robbie M., & Peters, Glen P. (2021). The Global Carbon Project's fossil CO2 emissions dataset [Data set]. " \
"Zenodo. https://doi.org/10.5281/zenodo.5569235."