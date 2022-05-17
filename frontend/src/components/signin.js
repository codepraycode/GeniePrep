import React from 'react';
import {Form, FormContent} from '../widgets/Form';
import Input from '../widgets/Form/input';
import Selection from '../widgets/Form/selection';
import Button from '../widgets/button';

const SignIn = () => {
    return (
        <div>

            <Form 
                submitTo={(e)=>{e.preventDefault()}} 
                error_info="Error Space" 
                
            >
                <FormContent inputHandler={(e)=>{console.log(e.target.name)}}>
                    <Input type="text" placeholder='Matric Number' name="matric_number"/>

                    <Input type="password" placeholder='Password' name="password"/>
                </FormContent>
                

                <div className="utils">
                    <Selection 
                        type="checkbox" 
                        inputHandler={()=>{}} 
                        name={"remember_me"} 
                        options={['remember_me']}
                    />

                    <a href="#">
                        Forgot Password?
                    </a>
                </div> 


                <Button text="Sign In" classes={"btn"}/>

            </Form>
        </div>
    );
};

export default SignIn;