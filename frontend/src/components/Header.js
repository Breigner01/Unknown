import { NavLink } from "react-router-dom";
import styled from "styled-components"

const Header = () => {

    return(
        <Wrapper>
            <Name>UHN-NOWN !Pa55w0rd Cracker</Name>
            <Links>
                <Link to="/">Generate Password</Link>
                <Link to="/checkPassword">Check Password</Link>
            </Links>
        </Wrapper>
    )
}

export default Header;

const Wrapper = styled.div `
color:	#a4f644;
position:sticky;
top:0;
background-color:#414767;
z-index:1000;
font-family: 'Share Tech Mono', monospace;
margin:10px;
width:100%;
display: flex;
flex-direction: row;
justify-content: space-between;
align-items: center;
box-shadow: 2px 9px 5px lightgrey;
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
background-color: #777;
height:80px;
border-radius: 10px;
}
&:hover {
    background-color: #777;
    height:80px;
    border-radius: 10px;
}
`

const Links = styled.div`
display: flex;
`
const Name = styled.h1``