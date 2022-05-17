import React from 'react';
// import { useParams } from 'react-router';
import { Link } from 'react-router-dom';
import Footer from '../components/footer';
import ResultHeader from '../components/result/header';
import ResultInfo from '../components/result/info';

const Result = () => {
    // const {id} = useParams();

    return (
        <div className='result container bg-white rounded-lg shadow-sm my-5 py-3'>
            {/* Result Header */}
            <ResultHeader/>

            <hr />

            {/* User Info */}

            <ResultInfo>
                <p className="text-muted ">User Information</p>

                <div className=" info">

                    <table className="table table-borderless">

                            <tbody>
                                <tr>

                                    <th scope="row">Matric Number:</th>
                                    <td>cpc/18/002</td>
                                </tr>

                                <tr>
                                    <th scope="row">Full Name:</th>
                                    <td>Candie Maletore</td>
                                </tr>

                                <tr>
                                    <th scope="row">Gender:</th>
                                    <td>Male</td>
                                </tr>

                                <tr>
                                    <th scope="row">Email</th>
                                    <td>candie@gmail.com</td>
                                </tr>

                            </tbody>
                        </table>
                </div>

            </ResultInfo>

            <hr/>
            {/* Test Info */}
            <ResultInfo>

                <p className="text-muted ">Test Information</p>

                <div className="row">

                    <div className="col">
                        
                        <table 
                            className="table table-borderless" 
                        >

                            <tbody>
                                <tr>
                                    <td><strong>Course</strong></td>
                                    <td colSpan="">Course 001</td>
                                </tr>
                                <tr>
                                    <td><strong>Scored</strong></td>
                                    
                                    <td colSpan="2">8</td>

                                    {/* <td>{{sum_percent|percent}}</td> */}
                                </tr>
                                <tr>
                                    <td><strong>Obtainable</strong></td>
                                    <td colSpan="3">10</td>
                                </tr>

                                <tr>
                                    <td><strong>% Score</strong></td>
                                    <td colSpan="3">80%</td>
                                </tr>
                                
                            </tbody>
                        </table>
                    </div>

                    <div className="col-md-5 col-sm-12 text-center">
                        <div className="progressbar" data-animate="false">
                            <div className="circle" data-percent="{{sum_percent | toWhole}}">
                                <div></div>

                            </div>
                        </div>

                    </div>
                </div>

            </ResultInfo>

            {/* Call to Action */}

            <div className="row text-center cta">
                <div className="col">
                    <Link
                        to="/dashboard" 
                        className="btn btn-warning shadow-sm"
                    > 
                        Go to Dashboard 
                    </Link>
                </div>

                <div className="col">
                    <Link
                        to="#" 
                        className="btn btn-warning shadow-sm"
                    > 
                        See Correction
                    </Link>
                </div>

                
                <div className="col">
                    <a 
                        href="#" 
                        className="btn btn-default text-black  shadow-sm"
                        onClick={(e)=>{
                            e.preventDefault();

                            window.print();
                        }}
                    >
                        Print slip 
                    </a>
                </div>

            </div>

            <Footer/>
        </div>
    );
};

export default Result;