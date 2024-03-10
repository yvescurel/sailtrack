    
    function getDateJJMMAAAAHHmm(myDate) {
    
        var today = new Date();
        var day = myDate.getDate() + "";
        var month = (myDate.getMonth() + 1) + "";
        var year = myDate.getFullYear() + "";
        var hour = myDate.getHours() + "";
        var minutes = myDate.getMinutes() + "";
        
        day = checkZero(day);
        month = checkZero(month);
        hour = checkZero(hour);
        minutes = checkZero(minutes);
        
        var d =  day + "/" + month + "/" + year + " " + hour + ":" + minutes;
        
        return d;
    
    }

    function getDateJJMMAAAAHHmmss(myDate) {
    
        var today = new Date();
        var day = myDate.getDate() + "";
        var month = (myDate.getMonth() + 1) + "";
        var year = myDate.getFullYear() + "";
        var hour = myDate.getHours() + "";
        var minutes = myDate.getMinutes() + "";
        var sec = myDate.getSeconds() + "";
        
        day = checkZero(day);
        month = checkZero(month);
        hour = checkZero(hour);
        minutes = checkZero(minutes);
        sec = checkZero(sec);
        
        var d =  day + "/" + month + "/" + year + " " + hour + ":" + minutes+ ":" + sec;
        
        return d;
    
    }
    
    function checkZero(data){
        if(data.length == 1){
        data = "0" + data;
        }
        return data;
    }

    function getDistanceKm(lat1, lon1, lat2, lon2) {
        const r = 6371; // km
        const p = Math.PI / 180;
        const a = 0.5 - Math.cos((lat2 - lat1) * p) / 2
                        + Math.cos(lat1 * p) * Math.cos(lat2 * p) *
                        (1 - Math.cos((lon2 - lon1) * p)) / 2;
        return 2 * r * Math.asin(Math.sqrt(a));
    }


    function radians(n) {
        return n * (Math.PI / 180);
    }
    function degrees(n) {
        return n * (180 / Math.PI);
    }
    function getBearing(startLat,startLong,endLat,endLong){
        startLat = radians(startLat);
        startLong = radians(startLong);
        endLat = radians(endLat);
        endLong = radians(endLong);

        var dLong = endLong - startLong;

        var dPhi = Math.log(Math.tan(endLat/2.0+Math.PI/4.0)/Math.tan(startLat/2.0+Math.PI/4.0));
        if (Math.abs(dLong) > Math.PI){
            if (dLong > 0.0)
            dLong = -(2.0 * Math.PI - dLong);
            else
            dLong = (2.0 * Math.PI + dLong);
        }

        return (degrees(Math.atan2(dLong, dPhi)) + 360.0) % 360.0;
    }

    function getSpeedMS(startTime,endTime,dist) {
        const elapsedTime = (endTime-startTime) / 1000; // In seconds
        const distance = dist;  // en metres
        const currentSpeed = distance / elapsedTime; // In meters / second
        return currentSpeed;
    }

    function getSpeedKH(startTime,endTime,dist) {
        const elapsedTime = (endTime-startTime) / 1000; // In seconds
        const distance = dist;  // en metres
        const currentSpeed = distance / elapsedTime; // In meters / second
        return currentSpeed * 3.6;
    }

    function getSpeedNoeuds(startTime,endTime,dist) {
        const elapsedTime = (endTime-startTime) / 1000; // In seconds
        const distance = dist;  // en metres
        const currentSpeed = distance / elapsedTime; // In meters / second
        return currentSpeed * 1.94384;
    }