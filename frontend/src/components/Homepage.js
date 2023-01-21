import styled from "styled-components";
import { useState } from "react";
import Slider from 'react-slider-simple';

const Homepage = () => {
    const [value, setValue] = useState(0);

    const handleChange = (newValue) => {
        setValue(Math.round(newValue))
    };

    const handleIncrease = () => {
        setValue(value + 1)
    }

    const handleDecrease = () => {
        setValue(value - 1)
    }


    return (
        <Wrapper>
            <Info>
                Instantly generate a secure random password with our tool
            </Info>
            <div>
                Customize your password
            </div>
            <length>
                Password Length:
                <input 
                value={value} />
                <button
                onClick={handleIncrease}> +
                </button>
                <button
                onClick={handleDecrease}> -
                </button>
            </length>
            <StyledSlider
                min={0} 
                max={100} 
                value={value} 
                onChange={handleChange} 
            />
            <p>Value: {value}</p>
        <CheckBoxes>
        <label>
            <input type="checkbox" name="uppercase" />
            Uppercase
        </label>
        <label>
            <input type="checkbox" name="lowercase" />
            Lowercase
        </label>
        <label>
            <input type="checkbox" name="numbers" />
            Numbers
        </label>
        <label>
            <input type="checkbox" name="special chars" /> 
            Special Characters
        </label>
        <label>
            <input type="checkbox" name="ambiguous" /> 
            Ambiguous 
        </label>
        </CheckBoxes>
        <Input type="text"/>
        <button 
        onClick={() =>  navigator.clipboard.writeText('Copy this text to clipboard')}>
            Copy
        </button>
        </Wrapper>

    )
}
const Wrapper = styled.div `
font-family: 'Share Tech Mono', monospace;
display:flex;
flex-direction:column;
justify-content: center;
align-items: center;
background-color:lightgoldenrodyellow;
padding:15px;

`
const Info = styled.div`
font-size:35px;
display: flex;
align-items: center;
`
const CheckBoxes = styled.div`
display:flex;
margin:2%;
`
const Input = styled.input`
height:80px;
width:450px;
border-radius: 15px;
border:none;
box-shadow: 2px 9px 5px lightgrey;
`
const StyledSlider = styled(Slider)`
    width: 500px;
    height: 50px;
    background-color: #ddd;
`
export default Homepage;