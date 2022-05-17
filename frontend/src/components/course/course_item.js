import React from 'react';
import {useNavigate} from 'react-router-dom';

const CourseItem = ({record, key}) => {
    const navigate = useNavigate();

    return(
    <div className="card course_item col" key={key} onClick={()=>{navigate('/test')}}>
        <p className="course_name"> 
            Course {record}
        </p>

        <div className="card-footer text-center">
            <span>Click To Pratise</span>
        </div>
    </div>
    )


    
};

export default CourseItem;