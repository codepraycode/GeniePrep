import React from 'react';
import {Form, FormContent} from '../widgets/Form';
import Input from '../widgets/Form/input';
import Selection from '../widgets/Form/selection';
import Button from '../widgets/button';

const SignUp = () => {
    return (
        <div>
            <Form 
                submitTo={(e)=>{e.preventDefault()}} 
                error_info="Error Space"    
            >
                <FormContent inputHandler={(e)=>{console.log(e.target.name)}}>
                    <Input type="text" placeholder='First Name' name="first_name"/>
                    <Input type="text" placeholder='Last Name' />

                    <Selection 
                        type="radio" 
                        inputHandler={()=>{}} 
                        name="gender" 
                        
                        options={['male','female']}
                    />

                    <Input type="email" placeholder='Email' />

                    <Input type="password" placeholder='Password' name="password"/>
                    <Input type="password" placeholder='Confirm Password' name="confirm_password"/>

                </FormContent>


                <Button text="Sign Up" type="submit"/>
            </Form>
        </div>
    );
};

export default SignUp;

/* 

 - First name
 - last name
 - gender
 - email
 -password
*/