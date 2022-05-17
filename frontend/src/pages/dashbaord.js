import React from 'react';

import Header from '../components/header';

import Courses from '../components/course/course_display';
import Records from '../components/records';
import Footer from '../components/footer';
import { Link } from 'react-router-dom';



const Dashboard = (props) => {
    return (
        <>
            <Header>
                <h2>Dashboard</h2>

                <div className="nav">
                    <ul>
                        <li>
                            <Link to={'#'}>
                                
                                <i className="fas fa-user"></i>
                            </Link>
                        </li>

                        <li>
                            <Link to={'/signin'} className="btn">
                                <i className="fas fa-solid fa-power-off"></i>
                            </Link>
                        </li>
                    </ul>
                </div>
            </Header>

            {/* Course Display */}
            <Courses/>

            <Records/>

            
            <Footer className="card"/>

        </>
        
    );
};

export default Dashboard;