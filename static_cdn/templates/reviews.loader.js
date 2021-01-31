var sheet = document.createElement('style');
const reviewsBackgroundColor = '{{campain.backgroundColor}}';
const reviewsHeadingColor = '{{campain.headingColor}}';
const reviewsTextColor = '{{campain.textColor}}';
const reviewsXOffset = '{{campain.xOffset}}';
const reviewsYOffset = '{{campain.yOffset}}';


const reviewsPosition = '{{campain.position}}';
var positionStyle='';
/**
 * 
 * left: calc(30px + ${reviewsXOffset});
    right: auto;
    bottom: ${reviewsYOffset};
    top: calc(11px + auto);
 */
debugger;
switch(reviewsPosition) {
    case "0": // left-bottom
        positionStyle = `left: calc(30px + ${reviewsXOffset});
        right: auto;
        bottom: ${reviewsYOffset};
        top: calc(11px + auto);`
        break;
    case "1": // left-top
        positionStyle = `left: calc(30px + ${reviewsXOffset});
        right: auto;
        bottom: calc(11px + auto);
        top: ${reviewsYOffset};`
        break;
    case "2": // right-botoom
        positionStyle = `left: auto;
        right: calc(30px + ${reviewsXOffset});
        bottom: ${reviewsYOffset};
        top: calc(11px + auto);`
        break;
    case "3": // right-top
        positionStyle = `left: auto;
        right: calc(30px + ${reviewsXOffset});
        bottom: calc(11px + auto);
        top: ${reviewsYOffset};`
        break;


}
console.log('positionStyle', positionStyle);

sheet.innerHTML = `
@keyframes slideOutAnimation {
    0% {
        transform: skew(0deg);
    }
    10% {
        transform: skew(-5deg);
    }
    20% {
        transform: skew(0deg) translate(0);
    }
    30% {
        transform: skew(-20deg);
    }
    38% {
        transform: skew(0deg) translateX(30px);
    }
    40% {
        transform: translateX(0px);
    }
    100%{
        transform: skewX(53deg) translateX(-500px);
        opacity: 0;
    }
}
@keyframes slideInAnimation {
    0%{
        transform: skewX(53deg) translateX(-500px);
        opacity: 0;
    }
    60% {
        transform: translateX(0px);
    }
    62% {
        transform: skew(0deg) translateX(30px);
    }
    70% {
        transform: skew(-20deg);
    }
    80% {
        transform: skew(0deg) translate(0);
    }
    90% {
        transform: skew(-5deg);
    }
    100% {
        transform: skew(0deg);
    }
}
.slideIn {
    animation:slideInAnimation;
}
.slideOut {
    animation:slideOutAnimation;
}

#reviewsProof {
    ${positionStyle}
    z-index: 2147483647;
    height: 90px;
    width: 340px;
    position: fixed;
    background-color: ${reviewsBackgroundColor};
    border: 2px solid #e8e8e8 !important;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-fill-mode: both;
    animation-fill-mode: both;
    padding: 5px;
    border-radius: 40px;
    -webkit-box-shadow: 2px 2px 20px #000;
    box-shadow: 2px 2px 20px #000;
    max-width:80vw;
  }
  
  #reviewsProof .reviews-proof-img {
    width: 110px;
    height: 110px;
    border-radius: 50%;
    position: absolute;
    background-color: #fff;
    top: -11px;
    left: -30px;
    border: 2px solid #e8e8e8 !important;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    z-index: 99;
  }
  
  #reviewsProof .reviews-proof-img img {
    width: 98px;
    height: 98px;
    border-radius: 50%;
    position: relative;
    top: 4px;
    left: 4px;
    z-index: 99;
  }
  
  #reviewsProof .reviews-proof-text {
    width: calc(100% - 10px);
    height: 82px;
    position: absolute;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }
  
  #reviewsProof .reviews-proof-text #close-proofs {
    width: 23px;
    height: 23px;
    line-height: 21px;
    border: 2px solid #f5f5f5 !important;
    border-radius: 50%;
    color: #fff;
    text-align: center;
    text-decoration: none;
    background: #464646;
    -webkit-box-shadow: 0 0 3px grey;
    box-shadow: 0 0 3px grey;
    font-size: 14px;
    position: absolute;
    right: -10px;
    top: -25px;
    opacity: 0.3;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }
  
  #reviewsProof .reviews-proof-text h3 {
    font-size: 14px !important;
    margin: 0 10px 0 70px !important;
    padding: 0px !important;
    color: ${reviewsHeadingColor};
    font-weight: bold;
    line-height: 16.25px !important;
    border-bottom: 1px solid #000000;
  }
  
  #reviewsProof .reviews-proof-text h4 {
    font-size: 13px !important;
    margin: 0 0 0 80px !important;
    padding: 0px !important;
    color: ${reviewsTextColor};
    font-weight: normal !important;
    line-height: 15px !important;
    word-wrap: break-word;
  }
  
  #reviewsProof .reviews-proof-text h5 {
    color: #999;
    display: block;
    font-size: 12px !important;
    line-height: 12px !important;
    margin: 0 0 0 80px !important;
    padding: 0 !important;
    position: absolute;
    bottom: 5px;
    width: 60%;
    font-weight: normal !important;
  }
  #reviewsProof .reviews-proof-text img {
    position: absolute;
  }
  {%for prof in campain.proofs.all %}
    document.querySelector('#reviews-proof-hidden-{{prof.id}}').background = "url({{prof.image.url}}) no-repeat -9999px -9999px";
  {%endfor%}
  /*# sourceMappingURL=load-campain-styles.css.map */`
document.body.append(sheet);

const root = document.createElement('div');
root.setAttribute('id', 'reviewsProof');


const reviewsStartDelay = {{campain.startDelay}};
const reviewsDisplayTime = {{campain.displayTime}};
const reviewsHideTime = {{campain.hideTime}};

var reviewsAllImages = [] // use for preload iamges

var proofsHtml = []; 
{%for prof in campain.proofs.all %}
debugger;
    var img=new Image();
    img.src="{{prof.image.url}}"
    proofsHtml.push(`
                <div id="reviews-proof-hidden-{{prof.id}}"></div>
                <div class="reviews-proof-img">
                    <img src="{{prof.image.url}}"
                        alt="">
                </div>
                <div class="reviews-proof-text"><span id="close-proofs" class="close">X</span>
                    <h3>{{prof.title}}</h3>
                    <h4>{{prof.message}}</h4>
                    <h5>{{prof.time}}</h5>
                    
            </div>
            `);
{% endfor %}


initLoop();

var currentReview = 0;
function hideProof() {
    console.log('hide proof');
    document.querySelector('#reviewsProof').className = "slideOut";
    setTimeout(showProof, reviewsHideTime*1000);
}
function showProof() {
    console.log('start loop');
    root.innerHTML = proofsHtml[currentReview%proofsHtml.length];
    root.className = "slideIn";
    root.style = 'display:block;'
    setTimeout(hideProof, reviewsDisplayTime*1000);
    root.querySelector('#close-proofs').addEventListener('click', ()=>{
        console.log('close me');
        root.style = 'display:none;'
    })
    document.body.append(root);
    currentReview+=1;
}

function initLoop() {
    console.log('init loop');
    
    setTimeout(showProof, reviewsStartDelay*1000);
}