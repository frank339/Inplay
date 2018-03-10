function BrowserCheck() {
	var b = navigator.appName
	var u = navigator.userAgent.toLowerCase()
	if (b=="Netscape") this.b = "ns"
	else if (b=="Microsoft Internet Explorer") this.b = "ie"
	else this.b = b
	this.v = parseInt(navigator.appVersion)
	this.ns = (this.b=="ns" && this.v>=4)
	this.ns4 = (this.b=="ns" && this.v==4)
	this.ns5 = (this.b=="ns" && this.v==5)
	this.ie = (this.b=="ie" && this.v>=4)
	this.ie4 = (u.indexOf('msie 4')>0)
	this.ie5 = (u.indexOf('msie 5')>0)
	if (this.ie5) this.v = 5
	this.min = (this.ns||this.ie)
	this.win = (u.indexOf('win')>0)
	this.mac = (u.indexOf('mac')>0)
}

// automatically create the "is" object
is = new BrowserCheck()

if (is.mac && is.ns && (is.v < 5)) {
	document.write('<link href="/common/css/macnn4.css" rel="stylesheet" type="text/css">');
} else if (is.mac && is.ns && (is.v = 6)) {
	document.write('<link href="/common/css/macnn6.css" rel="stylesheet" type="text/css">');
} else if (is.win && is.ns && (is.v < 5)) {
	document.write('<link href="/common/css/winnn4.css" rel="stylesheet" type="text/css">');
} else if (is.win && is.ns && (is.v > 4)) {
	document.write('<link href="/common/css/winnn6.css" rel="stylesheet" type="text/css">');
} else if (is.mac && is.ie5) {
	//for mac ie version 5 which uses macnn6.css style sheet
	document.write('<link href="/common/css/macnn6.css" rel="stylesheet" type="text/css">');
} else {
	document.write('<link href="/common/css/winie6.css" rel="stylesheet" type="text/css">');
}
