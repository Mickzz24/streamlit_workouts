import streamlit as st
import numpy as np
import pandas as pd
import sklearn 
import json

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVR, SVC
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import plotly.express as px
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from ydata_profiling.config import Settings
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components
import pkg_resources
import sweetviz as sv


st.sidebar.title("AUTOML Checker")
st.sidebar.subheader("Finds the model which perfectly suits your dataset")

col1, col2 = st.sidebar.columns([1, 1.5])

with col1:
    ml_type = st.selectbox("Which type of ML do you need?",["Select ML Type", "Classification", "Regression"])

with col2 :
    file = st.file_uploader("Upload the dataset", type= "csv", label_visibility= "collapsed")

if not file: 

    st.title("AUTOML Checker")

    with st.container():
        st.subheader("Machine Learning, without the repetitive work.")

        st.write(
            "Upload your dataset, explore what’s inside, prepare your data, "
            "train models, and compare their performance — all in one place."
        )

        st.caption("From raw data → to meaningful model insights.")


    st.divider()

    with st.container():
        st.subheader("How It Works")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("### 01 · Upload")
            st.write("Bring your CSV dataset and get started.")

        with c2:
            st.markdown("### 02 · Explore")
            st.write("Understand your dataset before building a model.")

        with c3:
            st.markdown("### 03 · Prepare")
            st.write("Handle missing values, outliers, and features.")

        c4, c5, c6 = st.columns(3)

        with c4:
            st.markdown("### 04 · Encode")
            st.write("Convert categorical data into model-ready features.")

        with c5:
            st.markdown("### 05 · Train")
            st.write("Try different machine learning algorithms.")

        with c6:
            st.markdown("### 06 · Compare")
            st.write("Evaluate how the selected models perform.")


    st.divider()

    with st.container():
        st.subheader("Why AutoML Checker?")

        st.write(
            "You don't need to build the entire machine learning workflow "
            "from scratch every time. AutoML Checker brings the essential "
            "steps together so you can spend less time repeating preprocessing "
            "and training code and more time understanding your data and model results."
        )


    st.divider()

    with st.container():
        st.subheader("Supported Machine Learning")

        c1, c2 = st.columns(2)

        with c1:
            st.markdown("### Classification")
            st.write(
                "Logistic Regression  •  Decision Tree  •  "
                "Random Forest  •  SVC  •  KNN"
            )

        with c2:
            st.markdown("### Regression")
            st.write(
                "Linear Regression  •  Decision Tree  •  "
                "Random Forest  •  SVR  •  KNN"
            )


    st.divider()

    with st.container():
        st.subheader("Ready to explore your data?")

        st.write(
            "Upload a dataset and start discovering what your data can tell you."
        )
if file:

        st.title("Data & Model Insights")

        tab1,tab2 = st.tabs([
            "Preprocessing",
            "Model Prediction"
        ])
        with tab1:

            subtab1, subtab2, subtab3 = st.tabs(
                [
                    "EDA",
                    "Feature Engineering",
                    "Encoding"
                ]
            )

        if file:
            df = pd.read_csv(file)
            # st.subheader("Data Preview")
            # st.dataframe(df)

        if file:
            features = df.columns.tolist()
            target = st.sidebar.selectbox("Select your target variable",features)
            features.remove(target)

            eda = st.sidebar.multiselect("Select an auto visualization ", ["Pandas Profiling", "Sweetviz"])

            with subtab1:
            
                st.subheader("EDA Analysis")
                def dataset_eda(df):

                    shape_of_df = df.shape
                    col_names = df.columns.tolist()
                    col_dtypes = df.dtypes
                    missing_val = df.isnull().sum()
                    dup_val = df.duplicated().sum()
                    uniq_val = df.nunique()
                    stat = df.describe()

                    return shape_of_df, missing_val, dup_val

                shape_of_df, missing_val, dup_val = dataset_eda(df)

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("Rows", shape_of_df[0])

                with col2:
                    st.metric("Columns", shape_of_df[1])

                with col3:
                    st.metric("Missing Values", missing_val.sum())

                with col4:
                    st.metric("Duplicate Rows", dup_val)

                if "Pandas Profiling" in eda:

                    config = Settings(
                        interactions={
                            "continuous": False,
                            "categorical": False
                        }
                    )

                    profile = ProfileReport(
                        df,
                        title="Profiling Report",
                        config=config
                    )

                    components.html(profile.to_html(), height=1000, scrolling=True)

                if "Sweetviz" in eda:
                    report = sv.analyze(df)
                    report.show_html("sweetviz_report.html", open_browser=False)

                    with open("sweetviz_report.html", "r", encoding="utf-8") as f:
                        report_html = f.read()

                    components.html(report_html, height=1000, scrolling=True)

            with subtab2:

                st.subheader("Feature Engineering")
                def column_info(df, target):
                    
                    num_cols = df.select_dtypes(include= np.number).columns.tolist()
                    cat_cols = df.select_dtypes(include= "object").columns.tolist()

                    if target in num_cols:
                        num_cols.remove(target)
                    elif target in cat_cols:
                        cat_cols.remove(target)

                    num_count = len(num_cols)
                    cat_count = len(cat_cols)

                    return num_cols, cat_cols

                num_cols, cat_cols = column_info(df,target)

                c1, c2, c3, c4 = st.columns(4)

                with c1:
                    st.metric("Numerical Features", len(num_cols))

                with c2 :
                    st.metric("Categorical Features", len(cat_cols))

                with c3:
                    st.metric("Total Features", len(cat_cols) + len(num_cols))

                with c4:
                    st.metric("Missing Values", df.isnull().sum().sum())

                st.subheader("Before Missing Values Imputation")
                st.dataframe(df)

                df_before = df.copy()

                missing_before = df_before.isnull().sum().sum()
                features_before = df_before.shape[1]

                def feat_engg(df, num_cols, cat_cols):

                    for col in num_cols:
                        if df[col].isnull().sum() > 0:
                            df[col] = df[col].fillna(df[col].mean())

                    for col in cat_cols:
                        if df[col].isnull().sum() > 0:
                            df[col] = df[col].fillna(df[col].mode()[0])


                    no_of_outliers_before = 0
                    no_of_outliers_after = 0

                    for col in num_cols:
                        Q1 = df[col].quantile(0.25)
                        Q3 = df[col].quantile(0.75)

                        IQR = Q3 - Q1

                        lower = Q1 - 1.5 * IQR
                        upper = Q3 + 1.5 * IQR

                        outliers_before = (df[col] < lower) | (df[col] > upper)

                        no_of_outliers_before += outliers_before.sum()

                        df[col] = df[col].clip(lower, upper)

                        outliers_after = (df[col] < lower) | (df[col] > upper)
                        
                        no_of_outliers_after += outliers_before.sum()

                        return df, no_of_outliers_after, no_of_outliers_before

                df, no_of_out_bef, no_of_out_after = feat_engg(df, num_cols, cat_cols)

                missing_after = df.isnull().sum().sum()
                features_after = df.shape[1]

                c3, c4, c5, c6 = st.columns(4)

                # with c1:
                #     st.metric("Features Before", features_before)

                # with c2:
                #     st.metric("Features After", features_after)

                with c3:
                    st.metric("Missing Values Before", missing_before )

                with c4:
                    st.metric("Missing Values After", missing_after)

                with c5:
                    st.metric("Outliers Before", no_of_out_bef)

                with c6:
                    st.metric("Outliers After", no_of_out_after)

                st.subheader("After Missing Values Imputation")
                st.dataframe(df)

            with subtab3:

                st.subheader("Encoding")

                st.subheader("Data Preview")

                st.dataframe(df)

                st.subheader("Encoding Result Using Rank")

                def frequency_rank(df, cat_cols):
                    for col in cat_cols:
                        values = df[col].value_counts()
                        mapping = values.rank(method="dense", ascending=True).astype(int).to_dict()
                        df[col] = df[col].map(mapping)

                    return df

                df = frequency_rank(df, cat_cols)

                st.dataframe(df)

                one_hot = st.sidebar.multiselect("Select features which mostly returns yes/no ",cat_cols)

                st.subheader("Encoding Result Using One- Hot")

                for col in one_hot:
                    cat_cols.remove(col)
                df = frequency_rank(df, cat_cols)   

                df = pd.get_dummies(
                    df,
                    columns= one_hot,
                    dtype= int
                )

                st.dataframe(df)

            with tab2:

                # Train-test split starts

                X = df.drop(target, axis= 1)
                y = df[target]

                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42 )

                if ml_type == 'Classification':
                    selected_models = st.sidebar.multiselect("Select the classification models", 
                                                        ["Logistic Regression", "Decision Tree Classifier", "Random Forest Classifier", "SVC", "KNN"])
                else:
                    selected_models = st.sidebar.multiselect("Selected Regression models",
                                                        ["Linear Regression", "Decision Tree Regressor", "Random Forest Regressor", "SVR", "KNN"])

                clas_models = {"Logistic Regression" :LogisticRegression(), "Decision Tree Classifier" :DecisionTreeClassifier(), "Random Forest Classifier" :RandomForestClassifier(), "SVC" :  SVC(), "KNN" : KNeighborsClassifier()}
                reg_models = {"Linear Regression" : LinearRegression(), "Decision Tree Regressor"  : DecisionTreeRegressor(), "Random Forest Regressor" : RandomForestRegressor(), "SVR"  : SVR(), "KNN" : KNeighborsRegressor()}

                if selected_models:
                    clicked = st.sidebar.button("Run the models")

                    if clicked:
                        if ml_type == 'Classification':

                            clas_result = {}

                            for models in selected_models:

                                model = clas_models[models]

                                model.fit(X_train, y_train)

                                y_pred = model.predict(X_test)

                                accuracy = accuracy_score(y_test, y_pred)
                                precision = precision_score(y_test, y_pred)
                                recall = recall_score(y_test, y_pred)
                                f1 = f1_score(y_test, y_pred)

                                clas_result[models] = {
                                    "Accuracy" : accuracy,
                                    "Precision" : precision,
                                    "Recall" : recall,
                                    "F1-Score" : f1
                                }

                            clas_result_df = pd.DataFrame(clas_result).T

                            # st.dataframe(clas_result_df)

                            best_model = clas_result_df.mean(axis=1).idxmax()
                            
                            fig = px.bar(
                            clas_result_df,
                            x= clas_result_df.index,
                            y=["Accuracy", "Precision", "Recall", "F1-Score"],
                            barmode="group",
                            title="Bivariate Analysis",
                            hover_data={
                                "value": ":.2f"
                            }
                            )

                            st.plotly_chart(fig)

                            st.success(f"Best Overall model : {best_model}")

                        else:

                            reg_results = {}

                            for models in selected_models:

                                model = reg_models[models]
                                
                                model.fit(X_train, y_train)
                                
                                y_pred = model.predict(X_test)

                                mae = mean_absolute_error(y_test, y_pred)
                                mse = mean_squared_error(y_test, y_pred)
                                rmse = np.sqrt(mse)

                                reg_results[models] = {
                                    "MAE" : mae,
                                    "MSE" : mse,
                                    "RMSE" : rmse,
                                }

                                reg_result_df = pd.DataFrame(reg_results).T

                                best_model = reg_result_df.mean(axis= 1).idxmin()

                                fig = px.bar(
                                            reg_result_df,
                                            x= reg_result_df.index,
                                            y=["MAE", "MSE", "RMSE"],
                                            barmode="group",
                                            title="Bivariate Analysis",
                                            hover_data={
                                                "value": ":.2f"
                                }
                                )
                                
                            st.plotly_chart(fig)
                                
                            st.success(f"Best Overall model : {best_model}")

        project_name = st.sidebar.text_input("Enter the Project name")

        save_button = st.sidebar.button("Save as project")

        if save_button:

            with open('projects.json','r') as f:

                projects = json.load(f)
                # st.sidebar.write(projects)

            for project in projects:
                if project["project_name"] == project_name:
                    st.sidebar.error("Project already exists, please provide a different name ")
                    break

            else:

                project_details = {
                    "project_name" : project_name,
                    "dataset" : file.name,
                    "target" : target,
                    "ml_type" : ml_type,
                    "models" : selected_models,
                }

                projects.append(project_details)

                with open("projects.json", "w") as f:
                    json.dump(projects, f)

                st.sidebar.success("Project saved successfully")




                



                                

                            
                                

                        










                        




                        









