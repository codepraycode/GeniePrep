import React from 'react';
import CourseItem from './course_item';

const Courses = () => {
    return (
        <div className="course_display section container">
                <h4 className="lead">Available Courses</h4>

                <div className="courses  row">
                    {
                        [0,1,2,3].map((each,i)=>{
                            return <CourseItem record={each} key={i}/>
                        })
                    }
                    
                </div>
            </div>
    );
};

export default Courses;