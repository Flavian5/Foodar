import React from 'react';
import StarRatings from 'react-star-ratings';

const card = (props) => {
    return (
        <div style={{backgroundColor: 'white', borderRadius: 5, padding: '15px 30px', position: 'relative'}}>
            <div className="flex-box">
                <div style={{height: 150, width: 150, border: '1px solid black'}}>
                    <img style={{objectFit: 'cover', height: '100%', width: '100%'}} src={'/images/survey_char.png'}/>
                </div>
                <div style={{display: 'inline-block', marginLeft: 20, color: '#8A8C9A', fontWeight: 500}}>
                    <p style={{fontSize: 20, marginTop: 0, marginBottom: 5}}>Kibo Sushi House $$</p>
                    <StarRatings
                        rating={2.403}
                        starDimension="25px"
                        starSpacing="2px"
                    />
                    <span style={{marginLeft: 20}}>200 reviews</span>
                    <div style={{borderLeft: '3px solid #D15214', paddingLeft: 15}}>
                        <p style={{marginBottom: 5}}>73 Charllote street and Bay</p>
                        <p style={{marginTop: 0, position: 'relative'}}>.6 km <span style={{color: '#B7D870', right: 0, position: 'absolute'}}>Open</span></p>
                    </div>
                </div>
                <div style={{position:'absolute', bottom: 20, fontSize: 15, color: '#8A8C9A', fontWeight: 500, right: 70}}>
                    <p style={{marginBottom: 5}}>Your friends liked this place</p>
                    <div className="flex-box">
                        <img style={{marginRight: 10, height: 58, width: 58, objectFit: 'cover', borderRadius: '50%'}} src={'https://cdn.stockphotosecrets.com/wp-content/uploads/2018/08/hide-the-pain-stockphoto-840x560.jpg'}/>
                        <img style={{marginRight: 10, height: 58, width: 58, objectFit: 'cover', borderRadius: '50%'}} src={'https://www.bolde.com/wp-content/uploads/2018/09/iStock-918377480-400x400.jpg'}/>
                        <img style={{height: 58, width: 58, objectFit: 'cover', borderRadius: '50%'}} src={'https://i.ytimg.com/vi/-QdfHMWsou0/maxresdefault.jpg'}/>

                    </div>
                </div>
                <button style={{position: 'absolute', right: 30}} className="foodar-btn-2">More</button>
            </div>
        </div>
    );
};

export default card;