import React from 'react';
import { Outlet,Link } from 'react-router-dom';
const Auth = () => {
    return (
        <div>
            <h3>Authentication Page</h3>
            <Link to="/signin">Login</Link>
            <Link to="/signup">Register</Link>
            <hr/>
            <Outlet/>
        </div>
    );
};

export default Auth;