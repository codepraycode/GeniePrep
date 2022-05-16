import React from 'react';
import {Routes, Route} from 'react-router-dom';

// Authentication
import Auth from './auth';
import SignIn from '../components/signin';
import SignUp from '../components/signup';

const Pages = () => {
    return (
        <Routes>
            {/* <Route path="/" element={<Auth/>}/> */}
            <Route path="/" element={<Auth/>}>
                <Route path="signin" element={<SignIn/>}/>
                <Route path="signup" element={<SignUp/>}/>
            </Route>

            <Route
                path="*"
                element={
                    <main style={{ padding: "1rem" }}>
                    <p>There's nothing here!</p>
                    </main>
                }
            />
        </Routes>
    );
};

export default Pages;