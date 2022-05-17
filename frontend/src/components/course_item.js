import React from 'react';

const CourseItem = ({record, key}) => {
    return(
    <div className="card course_item col" key={key}>
        <p className="course_name"> 
            Course {record}
        </p>

        <div className="card-footer text-center">
            <a href="#">Click To Pratise</a>
        </div>
    </div>
    )


    
};

export default CourseItem;