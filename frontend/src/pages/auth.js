import React from 'react';
import { Outlet,NavLink } from 'react-router-dom';
import Card from '../widgets/card';

const Auth = () => {
    return (
        <div className="auth_container">
            <Card extraclass={"auth_card"}>
                
                <h3>Genie Prep</h3>

                <div className="nav">
                    <NavLink 
                        to="/signin" 
                        // className='btn active'
                        className={({isActive})=>`btn ${isActive ? 'active':''}`}
                    >
                        Login
                    </NavLink>

                    <NavLink 
                        to="/signup" 
                        // className='btn'
                        className={({isActive})=>`btn ${isActive ? 'active':''}`}
                    >
                        Register
                    </NavLink>
                </div>

                <Outlet/>
            </Card>
        </div>
    );
};

export default Auth;