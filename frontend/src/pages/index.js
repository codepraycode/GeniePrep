import React from 'react';
import {Routes, Route} from 'react-router-dom';

// Authentication
import Auth from './auth';
import SignIn from '../components/signin';
import SignUp from '../components/signup';

// Dashboard
import Dashboard from './dashbaord';
// Test
import Practise from './practise';

// Result
import Result from './result';

const Pages = () => {
    return (
        <Routes>
            {/* <Route path="/" element={<Auth/>}/> */}
            <Route path="/" element={<Auth/>}>
                <Route path="signin" element={<SignIn/>}/>
                <Route path="signup" element={<SignUp/>}/>
            </Route>


            <Route path="dashboard" element={<Dashboard/>}/>

            <Route path="/result" element={<Result/>}>
                <Route path=":id" element={<Result/>}/>
                {/* <Route path=":id/correction" element={<Result/>}/> */}
            </Route>

            <Route path="test" element={<Practise/>}/>

            

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