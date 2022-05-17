// Input Supporting Text, Email, Password

import React from 'react'

const supported = ['text','email','password']

const Input = (props) => {

    const {type, inputHandler, name, ...rest} = props;

    // console.log(props)

    let template;

    if(!supported.includes(type)){
        template = <input type="text" placeholder="-----" readOnly />
    }


    template = <input type={type} name={name} {...rest} onChange={inputHandler}/>

    return (<div>
    {template}
    </div>)
}

export default Input
