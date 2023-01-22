import styled from "styled-components";
import { useState } from "react";
import Slider from 'react-slider-simple';
import axios from "axios";
import * as PropTypes from "prop-types";

function Length(props) {
    return null;
}

Length.propTypes = {children: PropTypes.node};
const Homepage = () => {
    const [value, setValue] = useState(0);
    const [uppercase, setUppercase] = useState(false);
    const [lowercase, setLowercase] = useState(false);
    const [numbers, setNumbers] = useState(false);
    const [specialChars, setSpecialChars] = useState(false);
    const [ambiguousChars, setAmbiguousChars] = useState(false);

    const handleChange = (newValue) => {
        setValue(Math.round(newValue))
    };

    const handleIncrease = () => {
        setValue(value + 1)
    }

    const handleDecrease = () => {
        setValue(value - 1)
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        const data = {
            value: value,
            uppercase: uppercase,
            lowercase: lowercase,
            numbers: numbers,
            specialChars: specialChars,
            ambiguousChars: ambiguousChars
        }
        console.log(data)
        fetch("http://localhost:5000/genPassword", {mode:'cors', body: JSON.stringify(data), method: "POST"})
        // axios({
        //     method: "post",
        //     url: "http://localhost:5000/",
        //     data: data
        // }).then((res) => {
        //     console.log(res)

        .catch(function (error) {
            console.log(error)
                if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.log(error.response.data);
      console.log(error.response.status);
      console.log(error.response.headers);}})

  }

    return (
        <Wrapper>
            <Info>
                Instantly generate a secure random password with our tool
            </Info>
            <div>
                Customize your password
            </div>
            <Length>
                Password Length:
                <input
                value={value} />
                <button
                onClick={handleIncrease}> +
                </button>
                <button
                onClick={handleDecrease}> -
                </button>
            </Length>
            <StyledSlider
                min={0}
                max={100}
                value={value}
                onChange={handleChange}
                thumbColor="rgb(164, 246, 68)"
                sliderPathColor="rgb(24, 24, 24)"
                shadowColor="rgb(164, 246, 68)"

            />
            <p>Value: {value}</p>
        <CheckBoxes>
            <form>
        <label>
        <input
            type="checkbox"
            name="uppercase"
            checked={uppercase}
            onChange={(e) => setUppercase(checked => !checked)} />
            Uppercase
        </label>
        <label>
            <input
                type="checkbox"
                name="lowercase"
                checked={lowercase}
                onChange={(e) => setLowercase(checked => !checked)} />
            Lowercase
        </label>
        <label>
            <input
                type="checkbox"
                name="numbers"
                checked={numbers}
                onChange={(e) => setNumbers(checked => !checked)} />
            Numbers
        </label>
        <label>
            <input
                type="checkbox"
                name="specialChars"
                checked={specialChars}
                onChange={(e) => setSpecialChars(checked => !checked)} />
            Special Characters
        </label>
        <label>
            <input
                type="checkbox"
                name="ambiguous"
                checked={ambiguousChars}
                onChange={(e) => setAmbiguousChars(checked => !checked)} />
            Ambiguous
        </label>
        <label>
            <button type="submit" value="Submit" onClick={handleSubmit}>Generate Password</button>
        </label>
        </form>
        </CheckBoxes>
        </Wrapper>
    )
}



const Wrapper = styled.div `
font-family: 'Share Tech Mono', monospace;
display:flex;
flex-direction:column;
justify-content: center;
align-items: center;
background-color:#121212;
padding:15px;
color:#a4f644;

`
const Info = styled.div`
font-size:35px;
display: flex;
align-items: center;
`
const CheckBoxes = styled.div`
display:flex;
margin:2%;
accent-color: #181818;
`
const Input = styled.input` 
height:80px;
width:450px;
border-radius: 15px;
border:none;
box-shadow: 2px 9px 5px lightgrey;
background-color:#181818;
`
const StyledSlider = styled(Slider)`
width: 500px;
height: 50px;
background-color: #121212;
`

export default Homepage;