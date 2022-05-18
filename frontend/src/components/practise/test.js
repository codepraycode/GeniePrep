import React from 'react';
import Header from '../header';
import Timer from './timer';
import Button from '../../widgets/button';
import Question from './question';
import Pagination from './pagination';

const Test = () => {
    return (
        <div className="test_container">
            <Header className="sticky-top ">
                
                <div>
                    <h1>Genie Prep</h1>
                    <p>Matric Number: Course 102</p>
                    <p>Course 102</p>
                </div>

                <div>
                    <Timer/>
                </div>
                
                

                    

                
            </Header>

            <div className="question_annswer card container">
                
                <Question/>

                <div className="cta">
                    <Button text="Previous"/>
                    <Button text="Next"/>
                </div>

            </div>


            <div className="pagination card container">
               <Pagination/>
            </div>


        </div>
        
        
    );
};

export default Test;