import React from 'react';
import Header from '../header';
import Button from '../../widgets/button';

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
                    <p className="timer">00:00</p>
                </div>

                    

                
            </Header>

            <div className="question_annswer card container">
                <div class="labels">
                    <p>Question 01</p>

                    <p>Index</p>
                </div>

                <div className="options">
                    <div className="option_item card selected">
                        This is an Option
                    </div>

                    <div className="option_item card">
                        This is an Option
                    </div>

                    <div className="option_item card">
                        This is an Option
                    </div>

                    <div className="option_item card">
                        This is an Option
                    </div>
                </div>


                <div className="cta">
                    <Button text="Previous"/>
                    <Button text="Next"/>
                </div>
            </div>


            <div className="pagination card container">
               <ul>
                   {[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18].map((each,i)=>{
                       return <li key={i}>{each}</li>
                   })}
               </ul>
            </div>
        </div>
        
        
    );
};

export default Test;