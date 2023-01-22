import { BrowserRouter, Routes, Route } from "react-router-dom";
import Homepage from "./Homepage";
import Header from "./Header";
import CheckPassword from "./CheckPassword";
import Info from "./Info";
import GlobalStyles from "./GlobalStyles";

const App =() => {

  return (
    <BrowserRouter>
    <GlobalStyles />
    <Header />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/checkPassword" element={<CheckPassword />} />
        <Route path="/info" element={<Info />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
