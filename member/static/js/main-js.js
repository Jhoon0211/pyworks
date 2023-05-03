// 디지털 시계
window.onload = function (){
    setInterval(setWatch, 1000);

    function setWatch(){
        let date = new Date(); //현재 날짜와 시간 생성
        let now = date.toLocaleTimeString(); //시간만 출력
        document.getElementById("demo").innerHTML = now;
    }
}