import { BrowserRouter, Routes, Route } from "react-router-dom";
import Homepage from "./Homepage";
import Header from "./Header";
import CheckPassword from "./CheckPassword";

const App =() => {

  return (
    <BrowserRouter>
    <Header />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/checkPassword" element={<CheckPassword />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
