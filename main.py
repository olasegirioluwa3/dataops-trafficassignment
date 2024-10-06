import streamlit as st
import pandas as pd
import base64

def main():
    st.title("XLSX File Sorter App")

    uploaded_file = st.file_uploader("Upload an XLSX file", type=["xlsx"])

    if uploaded_file is not None:
        # Allow users to select a sheet
        sheet_name = st.selectbox("Select a sheet", pd.ExcelFile(uploaded_file).sheet_names)

        # Read the selected sheet into a DataFrame
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

        # st.write(f"Original DataFrame (Sheet: {sheet_name}):")
        # st.write(df)

        # # Allow users to select a column for sorting
        # column_to_sort = st.selectbox("Select a column to sort by", df.columns)

        # # Sort the DataFrame based on the selected column
        # sorted_df = df.sort_values(by=column_to_sort)

        # st.write("Sorted DataFrame:")
        # st.write(sorted_df)

        # Download the sorted DataFrame as a new XLSX file
        # download_button_str = get_table_download_link(sorted_df)
        # st.markdown(download_button_str, unsafe_allow_html=True)

def get_table_download_link(df):
    # Generates a link allowing the DataFrame to be downloaded as an XLSX file.
    excel_buffer = df.to_excel(index=False, engine='openpyxl')
    b64 = base64.b64encode(excel_buffer).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="sorted_data.xlsx">Download Sorted Data</a>'
    return href

if __name__ == "__main__":
    main()
# student_id 4060
# school_id 123
# class_id primary-one 726
# session_id 131
# section_id 1487
