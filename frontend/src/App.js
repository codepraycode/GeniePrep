import React from "react";
// import Auth from "./pages/auth";
import {BrowserRouter} from 'react-router-dom';
import Pages from './pages';

export default function App(){
    return(
        <BrowserRouter>
            <Pages/>
        </BrowserRouter>
    )
}

/* 
    PAGES
    - Login/signup page
    - dashboard page
    - pratice, and pratice setup [age]
    - result page
 */