import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('Airline_Satisfaction.pkl', 'rb'))


def predict(input_data):
    # Process the input data and make predictions using your model
    prediction = model.predict(input_data)
    return prediction

def main():
    st.set_page_config(page_title="Airline Passenger Satisfaction App",layout="wide")
    st.markdown("<h1 style='text-align: center; color: blue;'>Airline Passenger Satisfaction</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>Enter the required details for prediction:</h3>", unsafe_allow_html=True)
    
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    #footer {visibility: hidden;}
    #</style> """, unsafe_allow_html=True)
    # Create input fields for the required features
    gender = st.selectbox('gender', ['Male', 'Female'])
    customer_type=st.selectbox('Customer Type',['Loyal Customer','Disloyal Customer'])
    Age=st.text_input("Age")
    type_of_travel=st.selectbox('Type of Travel',['Personal Travel','Business Travel'])
    Class=st.selectbox('Class',['Eco','Eco Plus','Business'])
    flight_dist=st.text_input("Flight Distance")
    wifi=st.radio("Inflight Wifi Service",["0",'1','2','3','4','5'])
    time=st.radio("Departure/Arrival time convenient",['0','1','2','3','4','5'])
    online_booking=st.radio("Ease of Online booking",['0','1','2','3','4','5'])
    gate_location=st.radio("Gate Location",['0','1','2','3','4','5'])
    food_drink=st.radio("Food and Drink",['0','1','2','3','4','5'])
    boarding=st.radio("Online Boarding",['0','1','2','3','4','5'])
    comfort=st.radio("Seat Comfort",['0','1','2','3','4','5'])
    entertainment=st.radio("Inflight Entertainment",['0','1','2','3','4','5'])
    on_board_service=st.radio("On_Board Service",['0','1','2','3','4','5'])
    leg_service=st.radio("Leg Room Service",['0','1','2','3','4','5'])
    baggage=st.radio("Baggage Handling",['0','1','2','3','4','5'])
    check_in=st.radio("Check_in Service",['0','1','2','3','4','5'])
    inflight_service=st.radio("Inflight Service",['0','1','2','3','4','5'])
    clean=st.radio("Cleanliness",['0','1','2','3','4','5'])
    departure=st.text_input("Departure Delay in Minutes")
    arrival=st.text_input("Arrival Delay in Minutes")
    
    if gender == 'Male':
        gender = 0 
    else:
        gender = 1
        
    if customer_type== 'Loyal Customer':
        customer_type = 0 
    else:
        customer_type=1
    
    if type_of_travel == 'Personal Travel':
        type_of_travel = 0 
    else:
        type_of_travel = 1
        
    if Class== 'Eco':
        Class = 0 
    elif Class == 'Eco Plus':
        Class=1 
    else:
        Class=2
        
    # Create a dictionary of input values
    input_data = {
        'gender': gender,
        'Customer Type': customer_type,
        'Age': Age,
        'Type of Travel': type_of_travel,
        'Class': Class,
        'Flight Distance': flight_dist,
        'Inflight Wifi Service': wifi,
        'Departure/Arrival time convenient': time,
        'Ease of Online booking': online_booking,
        'Gate Location': gate_location,
        'Food and Drink': food_drink,
        'Online Boarding': boarding,
        'Seat Comfort': comfort,
        'Inflight Entertainment': entertainment,
        'On_Board Service': on_board_service,
        'Leg Room Service': leg_service,
        'Baggage Handling': baggage,
        'Check_in Service': check_in,
        'Gate Location': gate_location,
        'Inflight Service': inflight_service,
        'Cleanliness': clean,
        'Departure Delay in Minutes': departure,
        'Arrival Delay in Minutes': arrival
    }
    
    # Convert input data to a DataFrame
    input_df = pd.DataFrame([input_data])
    
    if st.button('Predict'):
        prediction = predict(input_df)
        # Display the predicted result
        #st.write('Predicted Placement:', prediction[0])
        if prediction[0]==1:
            # Apply styling to the output message
            styled_message = "<p style='color: green; font-size: 20px;'>Satisfied</p>"
            st.markdown(styled_message, unsafe_allow_html=True)
            st.balloons()
        else:
            result=0
            # Apply styling to the output message
            styled_message = "<p style='color: red; font-size: 20px;'>Not Satisfied</p>"
            st.markdown(styled_message, unsafe_allow_html=True)
            
               

if __name__ == '__main__':
    main()
