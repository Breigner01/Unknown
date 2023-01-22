import styled from "styled-components";

const Info = () => {
    return (
        <Wrapper>
        <h1>How to make your password stronger</h1>
        <ol>
            <li>
                <h3>
                    Keep strong password
                </h3>
                    Always creating a password with a length between eight to twenty characters and using as 
                    many characters as you can is a very effective way to keep your password safe. If you can, 
                    try to make a blend of symbols, numbers, upper and lower case letters. This will make your password 
                    difficult to hack.
            </li>
            <li>
                <h3>
                Do not use identical password on different platforms
                </h3>
                Remember, when creating a new account or a new ID, do not use the same password you have for your e-mail or other online platforms. 
                It’s possible that you already have the same passwords for dozens of different websites. 
                The first step now is to fix that and try not to use the same password again. 
                This will protect your data from being leaked.
            </li>
            <li>
                <h3>
                Create untraceable passwords
                </h3>
                Try avoiding using words, phrases, and numbers that relate to yourself when creating a new password. 
                The reason for that is because this kind of information could be easily discovered from your social media. 
                For example, most people use their birthdays, anniversary dates, pets’ name, or their baby’s name for a password. 
                All these could become hints to a hacker.
            </li>
            <li>
                <h3>
                Always remember to log out
                </h3>
                You’re probably used to logging on to different devices all the time such as on your personal PC or smartphone.
                 This way you might end up remaining logged-in on many digital devices around you, it’s not safe because others may pick up your device and use your identity easily. 
                Therefore, signing out whenever you are switching devices is necessary, doing so will guarantee the safety of your data, and it will help you memorize your password.
            </li>

        </ol>
        </Wrapper>
    )

}

const Wrapper = styled.div`
background-color: black;
color:#a4f644;
padding:25px;
font-family: 'Share Tech Mono', monospace;
`
export default Info