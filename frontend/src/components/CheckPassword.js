import styled from "styled-components";
import {useState} from "react";
const CheckPassword = () => {
const handleSubmit = (event) => {
    event.preventDefault()
    const data = {
        password: password,
    }
    console.log(data)
}
    const [password, setPassword] = useState("");

    const handleChange = (event) => {
        setPassword(password => event.target.value);
    }

    return (
        <>
            <Wrapper>
                <form>
                    <Input type="text"
                           value={password}
                           onChange={handleChange} />
                    <Button type="submit" value="submit" onClick={handleSubmit}>Check Password</Button>
                </form>
            </Wrapper>
        </>
    )
}

export default CheckPassword;

const Wrapper = styled.div`
display: flex;
align-items: center;
justify-content: center;
background-color: #121212;

`
const Input = styled.input`
height:80px;
width:450px;
border-radius: 15px;
background-color: #181818;
color: #a4f644;
border:none;
border:solid 1px #a4f644;
box-shadow: 2px 9px 5px #181818;
&:active {border: solid 1px #a4f644;}
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

