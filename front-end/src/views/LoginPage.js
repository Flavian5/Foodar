import React, { Component } from 'react';
import './LoginPage.scss';

class Login extends Component {

    state = {
        username: "",
        password: ""
    }

    render() {
        return (
            <div className="main-container login-container" style={{}}>
                <div style={{height: '100%'}}>
                    <div className="login-form-container" style={{paddingTop: 50}}>
                        <img src="/images/logo.png" style={{width: 250}}/>
                        <form className="login-form" style={{marginTop: 50}}>
                            <div className="input_container">
                                <input data-lpignore="true" name="username" type="text" placeholder="Username"/>
                                {/* <img src="https://cdn4.iconfinder.com/data/icons/36-slim-icons/87/calender.png" id="username_input_img"/> */}
                            </div>
                            <div className="input_container" style={{marginTop: 30}}>
                                <input data-lpignore="true" name="password" type="password" placeholder="Password"/>
                                {/* <img src="https://cdn4.iconfinder.com/data/icons/36-slim-icons/87/calender.png" id="username_input_img"/> */}
                            </div>
                            <p style={{textAlign: 'right', cursor: 'pointer'}}>Sign Up</p>
                            <button style={{width: '100%', cursor: 'pointer'}} type="button" className="foodar-btn foodar-btn-reg">Login</button>
                            <p style={{textAlign: 'center'}}>Sign in with your social network</p>
                            <div className="flex-box" style={{marginBottom: 15}}>
                                <div className="flex-1" style={{paddingRight: 5}}>
                                    <hr />
                                </div>
                                <div className="flex-1" style={{paddingLeft: 5}}>
                                    <hr/>
                                </div>
                            </div>
                            <img style={{width: 70, marginRight: 20, cursor: 'pointer'}} src="/images/google_logo.png"/>
                            <img style={{width: 70, cursor: 'pointer'}} src="/images/fb_logo.png"/>
                        </form>
                    </div>
                </div>
            </div>
        );
    }
}

export default Login;