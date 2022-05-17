import React from 'react';
import { Outlet,Link } from 'react-router-dom';
const Auth = () => {
    return (
        <div>
            <h3>Authentication Page</h3>

            <div className="nav">
                <Link to="/signin">Login</Link>
            <Link to="/signup">Register</Link>
            </div>
            
            <hr/>
            <Outlet/>
        </div>
    );
};

export default Auth;