import styled from "styled-components";

const CheckPassword = () => {

    return (
        <>
            <Wrapper>
                <form>
                    <Input type="text"/>
                    <Button type="submit" value="submit">Check Password</Button>
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

`
const Input = styled.input`
height:80px;
width:450px;
border-radius: 15px;
border:none;
box-shadow: 2px 9px 5px lightgrey;
`
const Button = styled.button`
color:white;
background-color: red;
border:none;
border-radius: 10px;
font-size: 24px;
padding:20px 40px;
box-shadow: 2px 9px 5px lightgrey;
margin:25px;
`

