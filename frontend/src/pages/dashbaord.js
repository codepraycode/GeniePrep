import React from 'react';

import Header from '../components/header';

import Courses from '../components/course_display';
import Records from '../components/records';
import Footer from '../components/footer';



const Dashboard = (props) => {
    return (
        <>
            <Header>
                <h2>Dashboard</h2>

                <div className="nav">
                    <ul>
                        <li>
                            <span>
                                
                                <i className="fas fa-user"></i>
                            </span>
                        </li>

                        <li>
                            <span>
                                <i className="fas fa-solid fa-power-off"></i>
                            </span>
                        </li>
                    </ul>
                </div>
            </Header>

            {/* Course Display */}
            <Courses/>

            <Records/>

            
            <Footer/>

        </>
        
    );
};

export default Dashboard;