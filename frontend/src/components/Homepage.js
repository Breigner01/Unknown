import styled from "styled-components";
import { useState, useEffect } from "react";
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
    const [password, setPassword] = useState(null);

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
        fetch(`${process.env.REACT_APP_BACKEND_URL}/genPassword`, {mode: 'cors', body: JSON.stringify(data), method: "POST"})
            .then((res) => {
                res.json().then((data) => {
                    setPassword(data);
                    console.log(data.password);
                    console.log(data.time);
                    console.log(data.strength)
                })
            })

        .catch(function (error) {
            console.log(error);}
        )

}
    return (
        <>
        <Wrapper>
            <Info>
                Instantly generate a secure random password with our tool
            </Info>
            <Title>
                Customize your password
            </Title>
            <PLength>
                Password Length:
                <Value
                value={value} />
                <Btn
                onClick={handleIncrease}> +
                </Btn>
                <Btn
                onClick={handleDecrease}> -
                </Btn>
            </PLength>
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
            <Button type="submit" value="Submit" onClick={handleSubmit}>Generate Password</Button>
        </label>
        </form>
        </CheckBoxes>
        </Wrapper>
        <div>
            {!password ? <div></div>
            :
            <Details>
                <h2>Password Details</h2>
                <div>{password.password}</div>
                <div>{password.strength}</div>
                <div>{password.time}</div>
            </Details>
            }



        </div>
        </>
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
margin-top:10px;
width:99%;

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
const Button = styled.button`
font-family: 'Share Tech Mono', monospace;
font-weight: bolder;
color:black;
background-color: #a4f644;
border:none;
border-radius: 10px;
font-size: 24px;
padding:20px 40px;
box-shadow: 2px 9px 5px #121212;
margin:25px;
`
const PLength = styled.div`
font-family: 'Share Tech Mono', monospace;
color:#a4f644;
font-size: 20px;
`
const Btn = styled.button`
font-family: 'Share Tech Mono', monospace;
font-weight: bolder;
color:black;
background-color: #a4f644;
border:none;
border-radius: 50%;
font-size: 24px;
margin:5px;
`

const Value = styled.input`
background-color: black;
color:#a4f644;
margin:15px;
font-family: 'Share Tech Mono', monospace;
font-size: 24px;
width:100px;
`
const Title = styled.div`
text-decoration: underline;
font-size: 28px;
margin-top:25px;
`
const Details = styled.div`
background-color: black;
color:#a4f644;
margin:15px;
font-family: 'Share Tech Mono', monospace;
font-size: 24px;
`
export default Homepage;