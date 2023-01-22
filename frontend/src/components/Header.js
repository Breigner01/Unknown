import { NavLink } from "react-router-dom";
import styled from "styled-components"

const Header = () => {

    return(
        <Wrapper>
            <Name>UHN-NOWN !Pa55w0rd Checker</Name>
            <Links>
                <Link to="/">Generate Password</Link>
                <Link to="/checkPassword">Check Password</Link>
                <Link to="/info">Info</Link>
            </Links>
        </Wrapper>
    )
}

export default Header;

const Wrapper = styled.div `
color:	#a4f644;
position:sticky;
top:0;
background-color:#121212;
z-index:1000;
font-family: 'Share Tech Mono', monospace;
width:100%;
display: flex;
flex-direction: row;
justify-content: space-between;
align-items: center;
border-radius:15px;
padding:10px;
`
const Link = styled(NavLink)`
display:flex;
justify-content: center;
align-items: center;
font-size: 20px;
color:#a4f644;;
text-decoration: none;
transition: all 0.2s;
margin:5%;
&.active {
background-color: #181818;
height:80px;
border-radius: 10px;
}
&:hover {
    background-color: #181818;
    height:80px;
    border-radius: 10px;
}
`

const Links = styled.div`
display: flex;
`
const Name = styled.h1``
