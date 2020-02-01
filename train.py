<!DOCTYPE html>
<!-- saved from url=(0230)https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/2457f366-d634-482e-9504-3eced80d87ab -->
<html class="cookies cors history json video websockets es6object fetch localstorage"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style class="vjs-styles-defaults">
      .video-js {
        width: 300px;
        height: 150px;
      }

      .vjs-fluid {
        padding-top: 56.25%
      }
    </style><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"><title>AI Programming with Python - Udacity</title><link rel="stylesheet" href="./train_files/fonts.min.css"><link rel="stylesheet" href="./train_files/katex.min.css" crossorigin="anonymous"><meta name="Baiduspider" content="nofollow"><meta name="Baiduspider" content="noarchive"><link rel="apple-touch-icon" href="https://classroom.udacity.com/touch-icon.png"><link rel="manifest" href="https://classroom.udacity.com/manifest.json"><script type="text/javascript" src="./train_files/2059d2614a"></script><script src="./train_files/nr-spa-1099.min.js.download"></script><script type="text/javascript" async="" src="./train_files/linkid.js.download"></script><script type="text/javascript" async="" src="./train_files/analytics.js.download"></script><script type="text/javascript" async="" src="./train_files/av16vnft"></script><script type="text/javascript" async="" src="./train_files/blueshift.js.download"></script><script type="text/javascript" async="" src="./train_files/analytics.min.js.download"></script><script>window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(t){try{s.console&&console.log(t)}catch(e){}}var o,i=t("ee"),a=t(21),s={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(s.console=!0,o.indexOf("dev")!==-1&&(s.dev=!0),o.indexOf("nr_dev")!==-1&&(s.nrDev=!0))}catch(c){}s.nrDev&&i.on("internal-error",function(t){r(t.stack)}),s.dev&&i.on("fn-err",function(t,e,n){r(n.stack)}),s.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(s,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,s){try{l?l-=1:o(s||new UncaughtException(t,e,n),!0)}catch(f){try{i("ierr",[f,c.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function o(t,e){var n=e?null:c.now();i("err",[t,n])}var i=t("handle"),a=t(22),s=t("ee"),c=t("loader"),f=t("gos"),u=window.onerror,d=!1,p="nr@seenError",l=0;c.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(13),t(12),"addEventListener"in window&&t(6),c.xhrWrappable&&t(14),d=!0)}s.on("fn-start",function(t,e,n){d&&(l+=1)}),s.on("fn-err",function(t,e,n){d&&!n[p]&&(f(n,p,function(){return!0}),this.thrown=!0,o(n))}),s.on("fn-end",function(){d&&!this.thrown&&l>0&&(l-=1)}),s.on("internal-error",function(t){i("ierr",[t,c.now(),!0])})},{}],3:[function(t,e,n){t("loader").features.ins=!0},{}],4:[function(t,e,n){function r(){M++,N=y.hash,this[u]=g.now()}function o(){M--,y.hash!==N&&i(0,!0);var t=g.now();this[h]=~~this[h]+t-this[u],this[d]=t}function i(t,e){E.emit("newURL",[""+y,e])}function a(t,e){t.on(e,function(){this[e]=g.now()})}var s="-start",c="-end",f="-body",u="fn"+s,d="fn"+c,p="cb"+s,l="cb"+c,h="jsTime",m="fetch",v="addEventListener",w=window,y=w.location,g=t("loader");if(w[v]&&g.xhrWrappable){var b=t(10),x=t(11),E=t(8),O=t(6),P=t(13),R=t(7),T=t(14),L=t(9),j=t("ee"),S=j.get("tracer");t(15),g.features.spa=!0;var N,M=0;j.on(u,r),j.on(p,r),j.on(d,o),j.on(l,o),j.buffer([u,d,"xhr-done","xhr-resolved"]),O.buffer([u]),P.buffer(["setTimeout"+c,"clearTimeout"+s,u]),T.buffer([u,"new-xhr","send-xhr"+s]),R.buffer([m+s,m+"-done",m+f+s,m+f+c]),E.buffer(["newURL"]),b.buffer([u]),x.buffer(["propagate",p,l,"executor-err","resolve"+s]),S.buffer([u,"no-"+u]),L.buffer(["new-jsonp","cb-start","jsonp-error","jsonp-end"]),a(T,"send-xhr"+s),a(j,"xhr-resolved"),a(j,"xhr-done"),a(R,m+s),a(R,m+"-done"),a(L,"new-jsonp"),a(L,"jsonp-end"),a(L,"cb-start"),E.on("pushState-end",i),E.on("replaceState-end",i),w[v]("hashchange",i,!0),w[v]("load",i,!0),w[v]("popstate",function(){i(0,M>1)},!0)}},{}],5:[function(t,e,n){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var o=t("ee"),i=t("handle"),a=t(13),s=t(12),c="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",p="resource",l="-start",h="-end",m="fn"+l,v="fn"+h,w="bstTimer",y="pushState",g=t("loader");g.features.stn=!0,t(8);var b=NREUM.o.EV;o.on(m,function(t,e){var n=t[0];n instanceof b&&(this.bstStart=g.now())}),o.on(v,function(t,e){var n=t[0];n instanceof b&&i("bst",[n,e,this.bstStart,g.now()])}),a.on(m,function(t,e,n){this.bstStart=g.now(),this.bstType=n}),a.on(v,function(t,e){i(w,[e,this.bstStart,g.now(),this.bstType])}),s.on(m,function(){this.bstStart=g.now()}),s.on(v,function(t,e){i(w,[e,this.bstStart,g.now(),"requestAnimationFrame"])}),o.on(y+l,function(t){this.time=g.now(),this.startPath=location.pathname+location.hash}),o.on(y+h,function(t){i("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+c]?window.performance[f](u,function(t){i(d,[window.performance.getEntriesByType(p)]),window.performance["c"+c]()},!1):window.performance[f]("webkit"+u,function(t){i(d,[window.performance.getEntriesByType(p)]),window.performance["webkitC"+c]()},!1)),document[f]("scroll",r,{passive:!0}),document[f]("keypress",r,!1),document[f]("click",r,!1)}},{}],6:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&o(e)}function o(t){s.inPlace(t,[u,d],"-",i)}function i(t,e){return t[1]}var a=t("ee").get("events"),s=t(24)(a,!0),c=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1],r=c(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?s(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],7:[function(t,e,n){function r(t,e,n){var r=t[e];"function"==typeof r&&(t[e]=function(){var t=r.apply(this,arguments);return o.emit(n+"start",arguments,t),t.then(function(e){return o.emit(n+"end",[null,e],t),e},function(e){throw o.emit(n+"end",[e],t),e})})}var o=t("ee").get("fetch"),i=t(21);e.exports=o;var a=window,s="fetch-",c=s+"body-",f=["arrayBuffer","blob","json","text","formData"],u=a.Request,d=a.Response,p=a.fetch,l="prototype";u&&d&&p&&(i(f,function(t,e){r(u[l],e,c),r(d[l],e,c)}),r(a,"fetch",s),o.on(s+"end",function(t,e){var n=this;if(e){var r=e.headers.get("content-length");null!==r&&(n.rxSize=r),o.emit(s+"done",[null,e],n)}else o.emit(s+"done",[t],n)}))},{}],8:[function(t,e,n){var r=t("ee").get("history"),o=t(24)(r);e.exports=r,o.inPlace(window.history,["pushState","replaceState"],"-")},{}],9:[function(t,e,n){function r(t){function e(){c.emit("jsonp-end",[],p),t.removeEventListener("load",e,!1),t.removeEventListener("error",n,!1)}function n(){c.emit("jsonp-error",[],p),c.emit("jsonp-end",[],p),t.removeEventListener("load",e,!1),t.removeEventListener("error",n,!1)}var r=t&&"string"==typeof t.nodeName&&"script"===t.nodeName.toLowerCase();if(r){var o="function"==typeof t.addEventListener;if(o){var a=i(t.src);if(a){var u=s(a),d="function"==typeof u.parent[u.key];if(d){var p={};f.inPlace(u.parent,[u.key],"cb-",p),t.addEventListener("load",e,!1),t.addEventListener("error",n,!1),c.emit("new-jsonp",[t.src],p)}}}}}function o(){return"addEventListener"in window}function i(t){var e=t.match(u);return e?e[1]:null}function a(t,e){var n=t.match(p),r=n[1],o=n[3];return o?a(o,e[r]):e[r]}function s(t){var e=t.match(d);return e&&e.length>=3?{key:e[2],parent:a(e[1],window)}:{key:t,parent:window}}var c=t("ee").get("jsonp"),f=t(24)(c);if(e.exports=c,o()){var u=/[?&](?:callback|cb)=([^&#]+)/,d=/(.*)\.([^.]+)/,p=/^(\w+)(\.|$)(.*)$/,l=["appendChild","insertBefore","replaceChild"];f.inPlace(HTMLElement.prototype,l,"dom-"),f.inPlace(HTMLHeadElement.prototype,l,"dom-"),f.inPlace(HTMLBodyElement.prototype,l,"dom-"),c.on("dom-start",function(t){r(t[0])})}},{}],10:[function(t,e,n){var r=t("ee").get("mutation"),o=t(24)(r),i=NREUM.o.MO;e.exports=r,i&&(window.MutationObserver=function(t){return this instanceof i?new i(o(t,"fn-")):i.apply(this,arguments)},MutationObserver.prototype=i.prototype)},{}],11:[function(t,e,n){function r(t){var e=a.context(),n=s(t,"executor-",e),r=new f(n);return a.context(r).getCtx=function(){return e},a.emit("new-promise",[r,e],e),r}function o(t,e){return e}var i=t(24),a=t("ee").get("promise"),s=i(a),c=t(21),f=NREUM.o.PR;e.exports=a,f&&(window.Promise=r,["all","race"].forEach(function(t){var e=f[t];f[t]=function(n){function r(t){return function(){a.emit("propagate",[null,!o],i),o=o||!t}}var o=!1;c(n,function(e,n){Promise.resolve(n).then(r("all"===t),r(!1))});var i=e.apply(f,arguments),s=f.resolve(i);return s}}),["resolve","reject"].forEach(function(t){var e=f[t];f[t]=function(t){var n=e.apply(f,arguments);return t!==n&&a.emit("propagate",[t,!0],n),n}}),f.prototype["catch"]=function(t){return this.then(null,t)},f.prototype=Object.create(f.prototype,{constructor:{value:r}}),c(Object.getOwnPropertyNames(f),function(t,e){try{r[e]=f[e]}catch(n){}}),a.on("executor-start",function(t){t[0]=s(t[0],"resolve-",this),t[1]=s(t[1],"resolve-",this)}),a.on("executor-err",function(t,e,n){t[1](n)}),s.inPlace(f.prototype,["then"],"then-",o),a.on("then-start",function(t,e){this.promise=e,t[0]=s(t[0],"cb-",this),t[1]=s(t[1],"cb-",this)}),a.on("then-end",function(t,e,n){this.nextPromise=n;var r=this.promise;a.emit("propagate",[r,!0],n)}),a.on("cb-end",function(t,e,n){a.emit("propagate",[n,!0],this.nextPromise)}),a.on("propagate",function(t,e,n){this.getCtx&&!e||(this.getCtx=function(){if(t instanceof Promise)var e=a.context(t);return e&&e.getCtx?e.getCtx():this})}),r.toString=function(){return""+f})},{}],12:[function(t,e,n){var r=t("ee").get("raf"),o=t(24)(r),i="equestAnimationFrame";e.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],13:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function o(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var i=t("ee").get("timer"),a=t(24)(i),s="setTimeout",c="setInterval",f="clearTimeout",u="-start",d="-";e.exports=i,a.inPlace(window,[s,"setImmediate"],s+d),a.inPlace(window,[c],c+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(c+u,r),i.on(s+u,o)},{}],14:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",s)}function o(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,y,"fn-",s)}function i(t){g.push(t),h&&(x?x.then(a):v?v(a):(E=-E,O.data=E))}function a(){for(var t=0;t<g.length;t++)r([],g[t]);g.length&&(g=[])}function s(t,e){return e}function c(t,e){for(var n in t)e[n]=t[n];return e}t(6);var f=t("ee"),u=f.get("xhr"),d=t(24)(u),p=NREUM.o,l=p.XHR,h=p.MO,m=p.PR,v=p.SI,w="readystatechange",y=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],g=[];e.exports=u;var b=window.XMLHttpRequest=function(t){var e=new l(t);try{u.emit("new-xhr",[e],e),e.addEventListener(w,o,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(c(l,b),b.prototype=l.prototype,d.inPlace(b.prototype,["open","send"],"-xhr-",s),u.on("send-xhr-start",function(t,e){r(t,e),i(e)}),u.on("open-xhr-start",r),h){var x=m&&m.resolve();if(!v&&!m){var E=1,O=document.createTextNode(E);new h(a).observe(O,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===w||a()})},{}],15:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<d;r++)t.removeEventListener(u[r],this.listener,!1);if(!e.aborted){if(n.duration=a.now()-this.startTime,4===t.readyState){e.status=t.status;var i=o(t,this.lastSize);if(i&&(n.rxSize=i),this.sameOrigin){var c=t.getResponseHeader("X-NewRelic-App-Data");c&&(e.cat=c.split(", ").pop())}}else e.status=0;n.cbTime=this.cbTime,f.emit("xhr-done",[t],t),s("xhr",[e,n,this.startTime])}}}function o(t,e){var n=t.responseType;if("json"===n&&null!==e)return e;var r="arraybuffer"===n||"blob"===n||"json"===n?t.response:t.responseText;return h(r)}function i(t,e){var n=c(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.sameOrigin=n.sameOrigin}var a=t("loader");if(a.xhrWrappable){var s=t("handle"),c=t(16),f=t("ee"),u=["load","error","abort","timeout"],d=u.length,p=t("id"),l=t(19),h=t(18),m=window.XMLHttpRequest;a.features.xhr=!0,t(14),f.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,l&&(l>34||l<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),f.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),f.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid)}),f.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],o=this;if(n&&r){var i=h(r);i&&(n.txSize=i)}this.startTime=a.now(),this.listener=function(t){try{"abort"===t.type&&(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof e.onload))&&o.end(e)}catch(n){try{f.emit("internal-error",[n])}catch(r){}}};for(var s=0;s<d;s++)e.addEventListener(u[s],this.listener,!1)}),f.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),f.on("xhr-load-added",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),f.on("xhr-load-removed",function(t,e){var n=""+p(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),f.on("addEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-added",[t[1],t[2]],e)}),f.on("removeEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-removed",[t[1],t[2]],e)}),f.on("fn-start",function(t,e,n){e instanceof m&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),f.on("fn-end",function(t,e){this.xhrCbStart&&f.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,e],e)})}},{}],16:[function(t,e,n){e.exports=function(t){var e=document.createElement("a"),n=window.location,r={};e.href=t,r.port=e.port;var o=e.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=e.hostname||n.hostname,r.pathname=e.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!e.protocol||":"===e.protocol||e.protocol===n.protocol,a=e.hostname===document.domain&&e.port===n.port;return r.sameOrigin=i&&(!e.hostname||a),r}},{}],17:[function(t,e,n){function r(){}function o(t,e,n){return function(){return i(t,[f.now()].concat(s(arguments)),e?null:this,n),e?void 0:this}}var i=t("handle"),a=t(21),s=t(22),c=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],p="api-",l=p+"ixn-";a(d,function(t,e){u[e]=o(p+e,!0,"api")}),u.addPageAction=o(p+"addPageAction",!0),u.setCurrentRouteName=o(p+"routeName",!0),e.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(l+"tracer",[f.now(),t,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[f.now(),r,o],n),o)try{return e.apply(this,arguments)}catch(t){throw c.emit("fn-err",[arguments,this,t],n),t}finally{c.emit("fn-end",[f.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){h[e]=o(l+e)}),newrelic.noticeError=function(t){"string"==typeof t&&(t=new Error(t)),i("err",[t,f.now()])}},{}],18:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],19:[function(t,e,n){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),e.exports=r},{}],20:[function(t,e,n){function r(t,e){if(!o)return!1;if(t!==o)return!1;if(!e)return!0;if(!i)return!1;for(var n=i.split("."),r=e.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var s=navigator.userAgent,c=s.match(a);c&&s.indexOf("Chrome")===-1&&s.indexOf("Chromium")===-1&&(o="Safari",i=c[1])}e.exports={agent:o,version:i,match:r}},{}],21:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],22:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],23:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],24:[function(t,e,n){function r(t){return!(t&&t instanceof Function&&t.apply&&!t[a])}var o=t("ee"),i=t(22),a="nr@original",s=Object.prototype.hasOwnProperty,c=!1;e.exports=function(t,e){function n(t,e,n,o){function nrWrapper(){var r,a,s,c;try{a=this,r=i(arguments),s="function"==typeof n?n(r,a):n||{}}catch(f){p([f,"",[r,a,o],s])}u(e+"start",[r,a,o],s);try{return c=t.apply(a,r)}catch(d){throw u(e+"err",[r,a,d],s),d}finally{u(e+"end",[r,a,c],s)}}return r(t)?t:(e||(e=""),nrWrapper[a]=t,d(t,nrWrapper),nrWrapper)}function f(t,e,o,i){o||(o="");var a,s,c,f="-"===o.charAt(0);for(c=0;c<e.length;c++)s=e[c],a=t[s],r(a)||(t[s]=n(a,f?s+o:o,i,s))}function u(n,r,o){if(!c||e){var i=c;c=!0;try{t.emit(n,r,o,e)}catch(a){p([a,n,r,o])}c=i}}function d(t,e){if(Object.defineProperty&&Object.keys)try{var n=Object.keys(t);return n.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(r){p([r])}for(var o in t)s.call(t,o)&&(e[o]=t[o]);return e}function p(e){try{t.emit("internal-error",e)}catch(n){}}return t||(t=o),n.inPlace=f,n.flag=a,n}},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?c(t,s,i):i()}function n(n,r,o,i){if(!p.aborted||i){t&&t(n,r,o);for(var a=e(o),s=m(n),c=s.length,f=0;f<c;f++)s[f].apply(a,r);var d=u[g[n]];return d&&d.push([b,n,r,a]),a}}function l(t,e){y[t]=m(t).concat(e)}function h(t,e){var n=y[t];if(n)for(var r=0;r<n.length;r++)n[r]===e&&n.splice(r,1)}function m(t){return y[t]||[]}function v(t){return d[t]=d[t]||o(n)}function w(t,e){f(t,function(t,n){e=e||"feature",g[n]=e,e in u||(u[e]=[])})}var y={},g={},b={on:l,addEventListener:l,removeEventListener:h,emit:n,get:v,listeners:m,context:e,buffer:w,abort:a,aborted:!1};return b}function i(){return new r}function a(){(u.api||u.feature)&&(p.aborted=!0,u=p.backlog={})}var s="nr@context",c=t("gos"),f=t(21),u={},d={},p=e.exports=o();p.backlog=u},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!E++){var t=x.info=NREUM.info,e=l.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return u.abort();f(g,function(e,n){t[e]||(t[e]=n)}),c("mark",["onload",a()+x.offset],null,"api");var n=l.createElement("script");n.src="https://"+t.agent,e.parentNode.insertBefore(n,e)}}function o(){"complete"===l.readyState&&i()}function i(){c("mark",["domContent",a()+x.offset],null,"api")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(s=Math.max((new Date).getTime(),s))-x.offset}var s=(new Date).getTime(),c=t("handle"),f=t(21),u=t("ee"),d=t(20),p=window,l=p.document,h="addEventListener",m="attachEvent",v=p.XMLHttpRequest,w=v&&v.prototype;NREUM.o={ST:setTimeout,SI:p.setImmediate,CT:clearTimeout,XHR:v,REQ:p.Request,EV:p.Event,PR:p.Promise,MO:p.MutationObserver};var y=""+location,g={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-spa-1099.min.js"},b=v&&w&&w[h]&&!/CriOS/.test(navigator.userAgent),x=e.exports={offset:s,now:a,origin:y,features:{},xhrWrappable:b,userAgent:d};t(17),l[h]?(l[h]("DOMContentLoaded",i,!1),p[h]("load",r,!1)):(l[m]("onreadystatechange",o),p[m]("onload",r)),c("mark",["firstbyte",s],null,"api");var E=0,O=t(23)},{}]},{},["loader",2,15,5,3,4]);
    ;NREUM.info={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",licenseKey:"2059d2614a",applicationID:"17871435",sa:1}</script><script>!function(){var analytics=window.analytics=window.analytics||[];if(!analytics.initialize)if(analytics.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{analytics.invoked=!0;analytics.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","page","once","off","on"];analytics.factory=function(t){return function(){var e=Array.prototype.slice.call(arguments);e.unshift(t);analytics.push(e);return analytics}};for(var t=0;t<analytics.methods.length;t++){var e=analytics.methods[t];analytics[e]=analytics.factory(e)}analytics.load=function(t){var e=document.createElement("script");e.type="text/javascript";e.async=!0;e.src=("https:"===document.location.protocol?"https://":"http://")+"sgmt.udacity.com/analytics.js/v1/"+t+"/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(e,n)};analytics.SNIPPET_VERSION="3.1.0";
  }}();</script><link href="./train_files/11.c9969.css" rel="stylesheet"><link href="./train_files/app.8d3c8.css" rel="stylesheet"><style type="text/css">.input-range__slider {
  appearance: none;
  background: #3f51b5;
  border: 1px solid #3f51b5;
  border-radius: 100%;
  cursor: pointer;
  display: block;
  height: 1rem;
  margin-left: -0.5rem;
  margin-top: -0.65rem;
  outline: none;
  position: absolute;
  top: 50%;
  transition: transform 0.3s ease-out, box-shadow 0.3s ease-out;
  width: 1rem; }
  .input-range__slider:active {
    transform: scale(1.3); }
  .input-range__slider:focus {
    box-shadow: 0 0 0 5px rgba(63, 81, 181, 0.2); }
  .input-range--disabled .input-range__slider {
    background: #cccccc;
    border: 1px solid #cccccc;
    box-shadow: none;
    transform: none; }

.input-range__slider-container {
  transition: left 0.3s ease-out; }

.input-range__label {
  color: #aaaaaa;
  font-family: "Helvetica Neue", san-serif;
  font-size: 0.8rem;
  transform: translateZ(0);
  white-space: nowrap; }

.input-range__label--min,
.input-range__label--max {
  bottom: -1.4rem;
  position: absolute; }

.input-range__label--min {
  left: 0; }

.input-range__label--max {
  right: 0; }

.input-range__label--value {
  position: absolute;
  top: -1.8rem; }

.input-range__label-container {
  left: -50%;
  position: relative; }
  .input-range__label--max .input-range__label-container {
    left: 50%; }

.input-range__track {
  background: #eeeeee;
  border-radius: 0.3rem;
  cursor: pointer;
  display: block;
  height: 0.3rem;
  position: relative;
  transition: left 0.3s ease-out, width 0.3s ease-out; }
  .input-range--disabled .input-range__track {
    background: #eeeeee; }

.input-range__track--background {
  left: 0;
  margin-top: -0.15rem;
  position: absolute;
  right: 0;
  top: 50%; }

.input-range__track--active {
  background: #3f51b5; }

.input-range {
  height: 1rem;
  position: relative;
  width: 100%; }</style><style type="text/css">.rc-tooltip.rc-tooltip-zoom-enter,
.rc-tooltip.rc-tooltip-zoom-leave {
  display: block;
}
.rc-tooltip-zoom-enter,
.rc-tooltip-zoom-appear {
  opacity: 0;
  animation-duration: 0.3s;
  animation-fill-mode: both;
  animation-timing-function: cubic-bezier(0.18, 0.89, 0.32, 1.28);
  animation-play-state: paused;
}
.rc-tooltip-zoom-leave {
  animation-duration: 0.3s;
  animation-fill-mode: both;
  animation-timing-function: cubic-bezier(0.6, -0.3, 0.74, 0.05);
  animation-play-state: paused;
}
.rc-tooltip-zoom-enter.rc-tooltip-zoom-enter-active,
.rc-tooltip-zoom-appear.rc-tooltip-zoom-appear-active {
  animation-name: rcToolTipZoomIn;
  animation-play-state: running;
}
.rc-tooltip-zoom-leave.rc-tooltip-zoom-leave-active {
  animation-name: rcToolTipZoomOut;
  animation-play-state: running;
}
@keyframes rcToolTipZoomIn {
  0% {
    opacity: 0;
    transform-origin: 50% 50%;
    transform: scale(0, 0);
  }
  100% {
    opacity: 1;
    transform-origin: 50% 50%;
    transform: scale(1, 1);
  }
}
@keyframes rcToolTipZoomOut {
  0% {
    opacity: 1;
    transform-origin: 50% 50%;
    transform: scale(1, 1);
  }
  100% {
    opacity: 0;
    transform-origin: 50% 50%;
    transform: scale(0, 0);
  }
}
.rc-tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  visibility: visible;
  font-size: 12px;
  line-height: 1.5;
  opacity: 0.9;
}
.rc-tooltip-hidden {
  display: none;
}
.rc-tooltip-placement-top,
.rc-tooltip-placement-topLeft,
.rc-tooltip-placement-topRight {
  padding: 5px 0 9px 0;
}
.rc-tooltip-placement-right,
.rc-tooltip-placement-rightTop,
.rc-tooltip-placement-rightBottom {
  padding: 0 5px 0 9px;
}
.rc-tooltip-placement-bottom,
.rc-tooltip-placement-bottomLeft,
.rc-tooltip-placement-bottomRight {
  padding: 9px 0 5px 0;
}
.rc-tooltip-placement-left,
.rc-tooltip-placement-leftTop,
.rc-tooltip-placement-leftBottom {
  padding: 0 9px 0 5px;
}
.rc-tooltip-inner {
  padding: 8px 10px;
  color: #fff;
  text-align: left;
  text-decoration: none;
  background-color: #373737;
  border-radius: 6px;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.17);
  min-height: 34px;
}
.rc-tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.rc-tooltip-placement-top .rc-tooltip-arrow,
.rc-tooltip-placement-topLeft .rc-tooltip-arrow,
.rc-tooltip-placement-topRight .rc-tooltip-arrow {
  bottom: 4px;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #373737;
}
.rc-tooltip-placement-top .rc-tooltip-arrow {
  left: 50%;
}
.rc-tooltip-placement-topLeft .rc-tooltip-arrow {
  left: 15%;
}
.rc-tooltip-placement-topRight .rc-tooltip-arrow {
  right: 15%;
}
.rc-tooltip-placement-right .rc-tooltip-arrow,
.rc-tooltip-placement-rightTop .rc-tooltip-arrow,
.rc-tooltip-placement-rightBottom .rc-tooltip-arrow {
  left: 4px;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #373737;
}
.rc-tooltip-placement-right .rc-tooltip-arrow {
  top: 50%;
}
.rc-tooltip-placement-rightTop .rc-tooltip-arrow {
  top: 15%;
  margin-top: 0;
}
.rc-tooltip-placement-rightBottom .rc-tooltip-arrow {
  bottom: 15%;
}
.rc-tooltip-placement-left .rc-tooltip-arrow,
.rc-tooltip-placement-leftTop .rc-tooltip-arrow,
.rc-tooltip-placement-leftBottom .rc-tooltip-arrow {
  right: 4px;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #373737;
}
.rc-tooltip-placement-left .rc-tooltip-arrow {
  top: 50%;
}
.rc-tooltip-placement-leftTop .rc-tooltip-arrow {
  top: 15%;
  margin-top: 0;
}
.rc-tooltip-placement-leftBottom .rc-tooltip-arrow {
  bottom: 15%;
}
.rc-tooltip-placement-bottom .rc-tooltip-arrow,
.rc-tooltip-placement-bottomLeft .rc-tooltip-arrow,
.rc-tooltip-placement-bottomRight .rc-tooltip-arrow {
  top: 4px;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #373737;
}
.rc-tooltip-placement-bottom .rc-tooltip-arrow {
  left: 50%;
}
.rc-tooltip-placement-bottomLeft .rc-tooltip-arrow {
  left: 15%;
}
.rc-tooltip-placement-bottomRight .rc-tooltip-arrow {
  right: 15%;
}
</style><link rel="stylesheet" type="text/css" href="./train_files/0.63cd2.css"><script charset="utf-8" src="./train_files/vendors_routes-courses_routes-nanodegrees_routes-settings.e6261.js.download"></script><link rel="stylesheet" type="text/css" href="./train_files/2.d0881.css"><script charset="utf-8" src="./train_files/vendors_routes-courses_routes-nanodegrees.2aeea.js.download"></script><link rel="stylesheet" type="text/css" href="./train_files/14.54aae.css"><script charset="utf-8" src="./train_files/vendors_routes-nanodegrees.62e5d.js.download"></script><link rel="stylesheet" type="text/css" href="./train_files/1.527f7.css"><script charset="utf-8" src="./train_files/routes-courses_routes-nanodegrees.6eeac.js.download"></script><link rel="stylesheet" type="text/css" href="./train_files/8.036bc.css"><script charset="utf-8" src="./train_files/routes-nanodegrees.24b4c.js.download"></script><link rel="stylesheet" type="text/css" href="./train_files/10.240cb.css"><script charset="utf-8" src="./train_files/survey-modal.0766c.js.download"></script><link rel="stylesheet" type="text/css" href="./train_files/17.d80c2.css"><script charset="utf-8" src="./train_files/17.8f805.js.download"></script><style type="text/css">/*!
 *  Font Awesome 4.1.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
 @font-face{font-family:'FontAwesome';src:url(/images/fontawesome-webfont-25a32.eot);src:url(/images/fontawesome-webfont-25a32.eot?#iefix&v=4.1.0) format('embedded-opentype'),url(/images/fontawesome-webfont-fdf49.woff) format('woff'),url(/images/fontawesome-webfont-4f002.ttf) format('truetype'),url(/images/fontawesome-webfont-d7c63.svg#fontawesomeregular) format('svg');font-weight:normal;font-style:normal}.fa{display:inline-block;font-family:FontAwesome;font-style:normal;font-weight:normal;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.fa-lg{font-size:1.33333333em;line-height:.75em;vertical-align:-15%}.fa-2x{font-size:2em}.fa-3x{font-size:3em}.fa-4x{font-size:4em}.fa-5x{font-size:5em}.fa-fw{width:1.28571429em;text-align:center}.fa-ul{padding-left:0;margin-left:2.14285714em;list-style-type:none}.fa-ul>li{position:relative}.fa-li{position:absolute;left:-2.14285714em;width:2.14285714em;top:.14285714em;text-align:center}.fa-li.fa-lg{left:-1.85714286em}.fa-border{padding:.2em .25em .15em;border:solid .08em #eee;border-radius:.1em}.pull-right{float:right}.pull-left{float:left}.fa.pull-left{margin-right:.3em}.fa.pull-right{margin-left:.3em}.fa-spin{-webkit-animation:spin 2s infinite linear;-moz-animation:spin 2s infinite linear;-o-animation:spin 2s infinite linear;animation:spin 2s infinite linear}@-moz-keyframes spin{0%{-moz-transform:rotate(0deg)}100%{-moz-transform:rotate(359deg)}}@-webkit-keyframes spin{0%{-webkit-transform:rotate(0deg)}100%{-webkit-transform:rotate(359deg)}}@-o-keyframes spin{0%{-o-transform:rotate(0deg)}100%{-o-transform:rotate(359deg)}}@keyframes spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(359deg);transform:rotate(359deg)}}.fa-rotate-90{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=1);-webkit-transform:rotate(90deg);-moz-transform:rotate(90deg);-ms-transform:rotate(90deg);-o-transform:rotate(90deg);transform:rotate(90deg)}.fa-rotate-180{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=2);-webkit-transform:rotate(180deg);-moz-transform:rotate(180deg);-ms-transform:rotate(180deg);-o-transform:rotate(180deg);transform:rotate(180deg)}.fa-rotate-270{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=3);-webkit-transform:rotate(270deg);-moz-transform:rotate(270deg);-ms-transform:rotate(270deg);-o-transform:rotate(270deg);transform:rotate(270deg)}.fa-flip-horizontal{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);-webkit-transform:scale(-1, 1);-moz-transform:scale(-1, 1);-ms-transform:scale(-1, 1);-o-transform:scale(-1, 1);transform:scale(-1, 1)}.fa-flip-vertical{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);-webkit-transform:scale(1, -1);-moz-transform:scale(1, -1);-ms-transform:scale(1, -1);-o-transform:scale(1, -1);transform:scale(1, -1)}.fa-stack{position:relative;display:inline-block;width:2em;height:2em;line-height:2em;vertical-align:middle}.fa-stack-1x,.fa-stack-2x{position:absolute;left:0;width:100%;text-align:center}.fa-stack-1x{line-height:inherit}.fa-stack-2x{font-size:2em}.fa-inverse{color:#fff}.fa-glass:before{content:"\F000"}.fa-music:before{content:"\F001"}.fa-search:before{content:"\F002"}.fa-envelope-o:before{content:"\F003"}.fa-heart:before{content:"\F004"}.fa-star:before{content:"\F005"}.fa-star-o:before{content:"\F006"}.fa-user:before{content:"\F007"}.fa-film:before{content:"\F008"}.fa-th-large:before{content:"\F009"}.fa-th:before{content:"\F00A"}.fa-th-list:before{content:"\F00B"}.fa-check:before{content:"\F00C"}.fa-times:before{content:"\F00D"}.fa-search-plus:before{content:"\F00E"}.fa-search-minus:before{content:"\F010"}.fa-power-off:before{content:"\F011"}.fa-signal:before{content:"\F012"}.fa-gear:before,.fa-cog:before{content:"\F013"}.fa-trash-o:before{content:"\F014"}.fa-home:before{content:"\F015"}.fa-file-o:before{content:"\F016"}.fa-clock-o:before{content:"\F017"}.fa-road:before{content:"\F018"}.fa-download:before{content:"\F019"}.fa-arrow-circle-o-down:before{content:"\F01A"}.fa-arrow-circle-o-up:before{content:"\F01B"}.fa-inbox:before{content:"\F01C"}.fa-play-circle-o:before{content:"\F01D"}.fa-rotate-right:before,.fa-repeat:before{content:"\F01E"}.fa-refresh:before{content:"\F021"}.fa-list-alt:before{content:"\F022"}.fa-lock:before{content:"\F023"}.fa-flag:before{content:"\F024"}.fa-headphones:before{content:"\F025"}.fa-volume-off:before{content:"\F026"}.fa-volume-down:before{content:"\F027"}.fa-volume-up:before{content:"\F028"}.fa-qrcode:before{content:"\F029"}.fa-barcode:before{content:"\F02A"}.fa-tag:before{content:"\F02B"}.fa-tags:before{content:"\F02C"}.fa-book:before{content:"\F02D"}.fa-bookmark:before{content:"\F02E"}.fa-print:before{content:"\F02F"}.fa-camera:before{content:"\F030"}.fa-font:before{content:"\F031"}.fa-bold:before{content:"\F032"}.fa-italic:before{content:"\F033"}.fa-text-height:before{content:"\F034"}.fa-text-width:before{content:"\F035"}.fa-align-left:before{content:"\F036"}.fa-align-center:before{content:"\F037"}.fa-align-right:before{content:"\F038"}.fa-align-justify:before{content:"\F039"}.fa-list:before{content:"\F03A"}.fa-dedent:before,.fa-outdent:before{content:"\F03B"}.fa-indent:before{content:"\F03C"}.fa-video-camera:before{content:"\F03D"}.fa-photo:before,.fa-image:before,.fa-picture-o:before{content:"\F03E"}.fa-pencil:before{content:"\F040"}.fa-map-marker:before{content:"\F041"}.fa-adjust:before{content:"\F042"}.fa-tint:before{content:"\F043"}.fa-edit:before,.fa-pencil-square-o:before{content:"\F044"}.fa-share-square-o:before{content:"\F045"}.fa-check-square-o:before{content:"\F046"}.fa-arrows:before{content:"\F047"}.fa-step-backward:before{content:"\F048"}.fa-fast-backward:before{content:"\F049"}.fa-backward:before{content:"\F04A"}.fa-play:before{content:"\F04B"}.fa-pause:before{content:"\F04C"}.fa-stop:before{content:"\F04D"}.fa-forward:before{content:"\F04E"}.fa-fast-forward:before{content:"\F050"}.fa-step-forward:before{content:"\F051"}.fa-eject:before{content:"\F052"}.fa-chevron-left:before{content:"\F053"}.fa-chevron-right:before{content:"\F054"}.fa-plus-circle:before{content:"\F055"}.fa-minus-circle:before{content:"\F056"}.fa-times-circle:before{content:"\F057"}.fa-check-circle:before{content:"\F058"}.fa-question-circle:before{content:"\F059"}.fa-info-circle:before{content:"\F05A"}.fa-crosshairs:before{content:"\F05B"}.fa-times-circle-o:before{content:"\F05C"}.fa-check-circle-o:before{content:"\F05D"}.fa-ban:before{content:"\F05E"}.fa-arrow-left:before{content:"\F060"}.fa-arrow-right:before{content:"\F061"}.fa-arrow-up:before{content:"\F062"}.fa-arrow-down:before{content:"\F063"}.fa-mail-forward:before,.fa-share:before{content:"\F064"}.fa-expand:before{content:"\F065"}.fa-compress:before{content:"\F066"}.fa-plus:before{content:"\F067"}.fa-minus:before{content:"\F068"}.fa-asterisk:before{content:"\F069"}.fa-exclamation-circle:before{content:"\F06A"}.fa-gift:before{content:"\F06B"}.fa-leaf:before{content:"\F06C"}.fa-fire:before{content:"\F06D"}.fa-eye:before{content:"\F06E"}.fa-eye-slash:before{content:"\F070"}.fa-warning:before,.fa-exclamation-triangle:before{content:"\F071"}.fa-plane:before{content:"\F072"}.fa-calendar:before{content:"\F073"}.fa-random:before{content:"\F074"}.fa-comment:before{content:"\F075"}.fa-magnet:before{content:"\F076"}.fa-chevron-up:before{content:"\F077"}.fa-chevron-down:before{content:"\F078"}.fa-retweet:before{content:"\F079"}.fa-shopping-cart:before{content:"\F07A"}.fa-folder:before{content:"\F07B"}.fa-folder-open:before{content:"\F07C"}.fa-arrows-v:before{content:"\F07D"}.fa-arrows-h:before{content:"\F07E"}.fa-bar-chart-o:before{content:"\F080"}.fa-twitter-square:before{content:"\F081"}.fa-facebook-square:before{content:"\F082"}.fa-camera-retro:before{content:"\F083"}.fa-key:before{content:"\F084"}.fa-gears:before,.fa-cogs:before{content:"\F085"}.fa-comments:before{content:"\F086"}.fa-thumbs-o-up:before{content:"\F087"}.fa-thumbs-o-down:before{content:"\F088"}.fa-star-half:before{content:"\F089"}.fa-heart-o:before{content:"\F08A"}.fa-sign-out:before{content:"\F08B"}.fa-linkedin-square:before{content:"\F08C"}.fa-thumb-tack:before{content:"\F08D"}.fa-external-link:before{content:"\F08E"}.fa-sign-in:before{content:"\F090"}.fa-trophy:before{content:"\F091"}.fa-github-square:before{content:"\F092"}.fa-upload:before{content:"\F093"}.fa-lemon-o:before{content:"\F094"}.fa-phone:before{content:"\F095"}.fa-square-o:before{content:"\F096"}.fa-bookmark-o:before{content:"\F097"}.fa-phone-square:before{content:"\F098"}.fa-twitter:before{content:"\F099"}.fa-facebook:before{content:"\F09A"}.fa-github:before{content:"\F09B"}.fa-unlock:before{content:"\F09C"}.fa-credit-card:before{content:"\F09D"}.fa-rss:before{content:"\F09E"}.fa-hdd-o:before{content:"\F0A0"}.fa-bullhorn:before{content:"\F0A1"}.fa-bell:before{content:"\F0F3"}.fa-certificate:before{content:"\F0A3"}.fa-hand-o-right:before{content:"\F0A4"}.fa-hand-o-left:before{content:"\F0A5"}.fa-hand-o-up:before{content:"\F0A6"}.fa-hand-o-down:before{content:"\F0A7"}.fa-arrow-circle-left:before{content:"\F0A8"}.fa-arrow-circle-right:before{content:"\F0A9"}.fa-arrow-circle-up:before{content:"\F0AA"}.fa-arrow-circle-down:before{content:"\F0AB"}.fa-globe:before{content:"\F0AC"}.fa-wrench:before{content:"\F0AD"}.fa-tasks:before{content:"\F0AE"}.fa-filter:before{content:"\F0B0"}.fa-briefcase:before{content:"\F0B1"}.fa-arrows-alt:before{content:"\F0B2"}.fa-group:before,.fa-users:before{content:"\F0C0"}.fa-chain:before,.fa-link:before{content:"\F0C1"}.fa-cloud:before{content:"\F0C2"}.fa-flask:before{content:"\F0C3"}.fa-cut:before,.fa-scissors:before{content:"\F0C4"}.fa-copy:before,.fa-files-o:before{content:"\F0C5"}.fa-paperclip:before{content:"\F0C6"}.fa-save:before,.fa-floppy-o:before{content:"\F0C7"}.fa-square:before{content:"\F0C8"}.fa-navicon:before,.fa-reorder:before,.fa-bars:before{content:"\F0C9"}.fa-list-ul:before{content:"\F0CA"}.fa-list-ol:before{content:"\F0CB"}.fa-strikethrough:before{content:"\F0CC"}.fa-underline:before{content:"\F0CD"}.fa-table:before{content:"\F0CE"}.fa-magic:before{content:"\F0D0"}.fa-truck:before{content:"\F0D1"}.fa-pinterest:before{content:"\F0D2"}.fa-pinterest-square:before{content:"\F0D3"}.fa-google-plus-square:before{content:"\F0D4"}.fa-google-plus:before{content:"\F0D5"}.fa-money:before{content:"\F0D6"}.fa-caret-down:before{content:"\F0D7"}.fa-caret-up:before{content:"\F0D8"}.fa-caret-left:before{content:"\F0D9"}.fa-caret-right:before{content:"\F0DA"}.fa-columns:before{content:"\F0DB"}.fa-unsorted:before,.fa-sort:before{content:"\F0DC"}.fa-sort-down:before,.fa-sort-desc:before{content:"\F0DD"}.fa-sort-up:before,.fa-sort-asc:before{content:"\F0DE"}.fa-envelope:before{content:"\F0E0"}.fa-linkedin:before{content:"\F0E1"}.fa-rotate-left:before,.fa-undo:before{content:"\F0E2"}.fa-legal:before,.fa-gavel:before{content:"\F0E3"}.fa-dashboard:before,.fa-tachometer:before{content:"\F0E4"}.fa-comment-o:before{content:"\F0E5"}.fa-comments-o:before{content:"\F0E6"}.fa-flash:before,.fa-bolt:before{content:"\F0E7"}.fa-sitemap:before{content:"\F0E8"}.fa-umbrella:before{content:"\F0E9"}.fa-paste:before,.fa-clipboard:before{content:"\F0EA"}.fa-lightbulb-o:before{content:"\F0EB"}.fa-exchange:before{content:"\F0EC"}.fa-cloud-download:before{content:"\F0ED"}.fa-cloud-upload:before{content:"\F0EE"}.fa-user-md:before{content:"\F0F0"}.fa-stethoscope:before{content:"\F0F1"}.fa-suitcase:before{content:"\F0F2"}.fa-bell-o:before{content:"\F0A2"}.fa-coffee:before{content:"\F0F4"}.fa-cutlery:before{content:"\F0F5"}.fa-file-text-o:before{content:"\F0F6"}.fa-building-o:before{content:"\F0F7"}.fa-hospital-o:before{content:"\F0F8"}.fa-ambulance:before{content:"\F0F9"}.fa-medkit:before{content:"\F0FA"}.fa-fighter-jet:before{content:"\F0FB"}.fa-beer:before{content:"\F0FC"}.fa-h-square:before{content:"\F0FD"}.fa-plus-square:before{content:"\F0FE"}.fa-angle-double-left:before{content:"\F100"}.fa-angle-double-right:before{content:"\F101"}.fa-angle-double-up:before{content:"\F102"}.fa-angle-double-down:before{content:"\F103"}.fa-angle-left:before{content:"\F104"}.fa-angle-right:before{content:"\F105"}.fa-angle-up:before{content:"\F106"}.fa-angle-down:before{content:"\F107"}.fa-desktop:before{content:"\F108"}.fa-laptop:before{content:"\F109"}.fa-tablet:before{content:"\F10A"}.fa-mobile-phone:before,.fa-mobile:before{content:"\F10B"}.fa-circle-o:before{content:"\F10C"}.fa-quote-left:before{content:"\F10D"}.fa-quote-right:before{content:"\F10E"}.fa-spinner:before{content:"\F110"}.fa-circle:before{content:"\F111"}.fa-mail-reply:before,.fa-reply:before{content:"\F112"}.fa-github-alt:before{content:"\F113"}.fa-folder-o:before{content:"\F114"}.fa-folder-open-o:before{content:"\F115"}.fa-smile-o:before{content:"\F118"}.fa-frown-o:before{content:"\F119"}.fa-meh-o:before{content:"\F11A"}.fa-gamepad:before{content:"\F11B"}.fa-keyboard-o:before{content:"\F11C"}.fa-flag-o:before{content:"\F11D"}.fa-flag-checkered:before{content:"\F11E"}.fa-terminal:before{content:"\F120"}.fa-code:before{content:"\F121"}.fa-mail-reply-all:before,.fa-reply-all:before{content:"\F122"}.fa-star-half-empty:before,.fa-star-half-full:before,.fa-star-half-o:before{content:"\F123"}.fa-location-arrow:before{content:"\F124"}.fa-crop:before{content:"\F125"}.fa-code-fork:before{content:"\F126"}.fa-unlink:before,.fa-chain-broken:before{content:"\F127"}.fa-question:before{content:"\F128"}.fa-info:before{content:"\F129"}.fa-exclamation:before{content:"\F12A"}.fa-superscript:before{content:"\F12B"}.fa-subscript:before{content:"\F12C"}.fa-eraser:before{content:"\F12D"}.fa-puzzle-piece:before{content:"\F12E"}.fa-microphone:before{content:"\F130"}.fa-microphone-slash:before{content:"\F131"}.fa-shield:before{content:"\F132"}.fa-calendar-o:before{content:"\F133"}.fa-fire-extinguisher:before{content:"\F134"}.fa-rocket:before{content:"\F135"}.fa-maxcdn:before{content:"\F136"}.fa-chevron-circle-left:before{content:"\F137"}.fa-chevron-circle-right:before{content:"\F138"}.fa-chevron-circle-up:before{content:"\F139"}.fa-chevron-circle-down:before{content:"\F13A"}.fa-html5:before{content:"\F13B"}.fa-css3:before{content:"\F13C"}.fa-anchor:before{content:"\F13D"}.fa-unlock-alt:before{content:"\F13E"}.fa-bullseye:before{content:"\F140"}.fa-ellipsis-h:before{content:"\F141"}.fa-ellipsis-v:before{content:"\F142"}.fa-rss-square:before{content:"\F143"}.fa-play-circle:before{content:"\F144"}.fa-ticket:before{content:"\F145"}.fa-minus-square:before{content:"\F146"}.fa-minus-square-o:before{content:"\F147"}.fa-level-up:before{content:"\F148"}.fa-level-down:before{content:"\F149"}.fa-check-square:before{content:"\F14A"}.fa-pencil-square:before{content:"\F14B"}.fa-external-link-square:before{content:"\F14C"}.fa-share-square:before{content:"\F14D"}.fa-compass:before{content:"\F14E"}.fa-toggle-down:before,.fa-caret-square-o-down:before{content:"\F150"}.fa-toggle-up:before,.fa-caret-square-o-up:before{content:"\F151"}.fa-toggle-right:before,.fa-caret-square-o-right:before{content:"\F152"}.fa-euro:before,.fa-eur:before{content:"\F153"}.fa-gbp:before{content:"\F154"}.fa-dollar:before,.fa-usd:before{content:"\F155"}.fa-rupee:before,.fa-inr:before{content:"\F156"}.fa-cny:before,.fa-rmb:before,.fa-yen:before,.fa-jpy:before{content:"\F157"}.fa-ruble:before,.fa-rouble:before,.fa-rub:before{content:"\F158"}.fa-won:before,.fa-krw:before{content:"\F159"}.fa-bitcoin:before,.fa-btc:before{content:"\F15A"}.fa-file:before{content:"\F15B"}.fa-file-text:before{content:"\F15C"}.fa-sort-alpha-asc:before{content:"\F15D"}.fa-sort-alpha-desc:before{content:"\F15E"}.fa-sort-amount-asc:before{content:"\F160"}.fa-sort-amount-desc:before{content:"\F161"}.fa-sort-numeric-asc:before{content:"\F162"}.fa-sort-numeric-desc:before{content:"\F163"}.fa-thumbs-up:before{content:"\F164"}.fa-thumbs-down:before{content:"\F165"}.fa-youtube-square:before{content:"\F166"}.fa-youtube:before{content:"\F167"}.fa-xing:before{content:"\F168"}.fa-xing-square:before{content:"\F169"}.fa-youtube-play:before{content:"\F16A"}.fa-dropbox:before{content:"\F16B"}.fa-stack-overflow:before{content:"\F16C"}.fa-instagram:before{content:"\F16D"}.fa-flickr:before{content:"\F16E"}.fa-adn:before{content:"\F170"}.fa-bitbucket:before{content:"\F171"}.fa-bitbucket-square:before{content:"\F172"}.fa-tumblr:before{content:"\F173"}.fa-tumblr-square:before{content:"\F174"}.fa-long-arrow-down:before{content:"\F175"}.fa-long-arrow-up:before{content:"\F176"}.fa-long-arrow-left:before{content:"\F177"}.fa-long-arrow-right:before{content:"\F178"}.fa-apple:before{content:"\F179"}.fa-windows:before{content:"\F17A"}.fa-android:before{content:"\F17B"}.fa-linux:before{content:"\F17C"}.fa-dribbble:before{content:"\F17D"}.fa-skype:before{content:"\F17E"}.fa-foursquare:before{content:"\F180"}.fa-trello:before{content:"\F181"}.fa-female:before{content:"\F182"}.fa-male:before{content:"\F183"}.fa-gittip:before{content:"\F184"}.fa-sun-o:before{content:"\F185"}.fa-moon-o:before{content:"\F186"}.fa-archive:before{content:"\F187"}.fa-bug:before{content:"\F188"}.fa-vk:before{content:"\F189"}.fa-weibo:before{content:"\F18A"}.fa-renren:before{content:"\F18B"}.fa-pagelines:before{content:"\F18C"}.fa-stack-exchange:before{content:"\F18D"}.fa-arrow-circle-o-right:before{content:"\F18E"}.fa-arrow-circle-o-left:before{content:"\F190"}.fa-toggle-left:before,.fa-caret-square-o-left:before{content:"\F191"}.fa-dot-circle-o:before{content:"\F192"}.fa-wheelchair:before{content:"\F193"}.fa-vimeo-square:before{content:"\F194"}.fa-turkish-lira:before,.fa-try:before{content:"\F195"}.fa-plus-square-o:before{content:"\F196"}.fa-space-shuttle:before{content:"\F197"}.fa-slack:before{content:"\F198"}.fa-envelope-square:before{content:"\F199"}.fa-wordpress:before{content:"\F19A"}.fa-openid:before{content:"\F19B"}.fa-institution:before,.fa-bank:before,.fa-university:before{content:"\F19C"}.fa-mortar-board:before,.fa-graduation-cap:before{content:"\F19D"}.fa-yahoo:before{content:"\F19E"}.fa-google:before{content:"\F1A0"}.fa-reddit:before{content:"\F1A1"}.fa-reddit-square:before{content:"\F1A2"}.fa-stumbleupon-circle:before{content:"\F1A3"}.fa-stumbleupon:before{content:"\F1A4"}.fa-delicious:before{content:"\F1A5"}.fa-digg:before{content:"\F1A6"}.fa-pied-piper-square:before,.fa-pied-piper:before{content:"\F1A7"}.fa-pied-piper-alt:before{content:"\F1A8"}.fa-drupal:before{content:"\F1A9"}.fa-joomla:before{content:"\F1AA"}.fa-language:before{content:"\F1AB"}.fa-fax:before{content:"\F1AC"}.fa-building:before{content:"\F1AD"}.fa-child:before{content:"\F1AE"}.fa-paw:before{content:"\F1B0"}.fa-spoon:before{content:"\F1B1"}.fa-cube:before{content:"\F1B2"}.fa-cubes:before{content:"\F1B3"}.fa-behance:before{content:"\F1B4"}.fa-behance-square:before{content:"\F1B5"}.fa-steam:before{content:"\F1B6"}.fa-steam-square:before{content:"\F1B7"}.fa-recycle:before{content:"\F1B8"}.fa-automobile:before,.fa-car:before{content:"\F1B9"}.fa-cab:before,.fa-taxi:before{content:"\F1BA"}.fa-tree:before{content:"\F1BB"}.fa-spotify:before{content:"\F1BC"}.fa-deviantart:before{content:"\F1BD"}.fa-soundcloud:before{content:"\F1BE"}.fa-database:before{content:"\F1C0"}.fa-file-pdf-o:before{content:"\F1C1"}.fa-file-word-o:before{content:"\F1C2"}.fa-file-excel-o:before{content:"\F1C3"}.fa-file-powerpoint-o:before{content:"\F1C4"}.fa-file-photo-o:before,.fa-file-picture-o:before,.fa-file-image-o:before{content:"\F1C5"}.fa-file-zip-o:before,.fa-file-archive-o:before{content:"\F1C6"}.fa-file-sound-o:before,.fa-file-audio-o:before{content:"\F1C7"}.fa-file-movie-o:before,.fa-file-video-o:before{content:"\F1C8"}.fa-file-code-o:before{content:"\F1C9"}.fa-vine:before{content:"\F1CA"}.fa-codepen:before{content:"\F1CB"}.fa-jsfiddle:before{content:"\F1CC"}.fa-life-bouy:before,.fa-life-saver:before,.fa-support:before,.fa-life-ring:before{content:"\F1CD"}.fa-circle-o-notch:before{content:"\F1CE"}.fa-ra:before,.fa-rebel:before{content:"\F1D0"}.fa-ge:before,.fa-empire:before{content:"\F1D1"}.fa-git-square:before{content:"\F1D2"}.fa-git:before{content:"\F1D3"}.fa-hacker-news:before{content:"\F1D4"}.fa-tencent-weibo:before{content:"\F1D5"}.fa-qq:before{content:"\F1D6"}.fa-wechat:before,.fa-weixin:before{content:"\F1D7"}.fa-send:before,.fa-paper-plane:before{content:"\F1D8"}.fa-send-o:before,.fa-paper-plane-o:before{content:"\F1D9"}.fa-history:before{content:"\F1DA"}.fa-circle-thin:before{content:"\F1DB"}.fa-header:before{content:"\F1DC"}.fa-paragraph:before{content:"\F1DD"}.fa-sliders:before{content:"\F1DE"}.fa-share-alt:before{content:"\F1E0"}.fa-share-alt-square:before{content:"\F1E1"}.fa-bomb:before{content:"\F1E2"}
</style><style type="text/css">/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */

/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */

.scoped-bootstrap {
  font-family: sans-serif;
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
}

.scoped-bootstrap {
  margin: 0;
}

.scoped-bootstrap article,
.scoped-bootstrap aside,
.scoped-bootstrap details,
.scoped-bootstrap figcaption,
.scoped-bootstrap figure,
.scoped-bootstrap footer,
.scoped-bootstrap header,
.scoped-bootstrap hgroup,
.scoped-bootstrap main,
.scoped-bootstrap menu,
.scoped-bootstrap nav,
.scoped-bootstrap section,
.scoped-bootstrap summary {
  display: block;
}

.scoped-bootstrap audio,
.scoped-bootstrap canvas,
.scoped-bootstrap progress,
.scoped-bootstrap video {
  display: inline-block;
  vertical-align: baseline;
}

.scoped-bootstrap audio:not([controls]) {
  display: none;
  height: 0;
}

.scoped-bootstrap [hidden],
.scoped-bootstrap template {
  display: none;
}

.scoped-bootstrap a {
  background-color: transparent;
}

.scoped-bootstrap a:active,
.scoped-bootstrap a:hover {
  outline: 0;
}

.scoped-bootstrap abbr[title] {
  border-bottom: 1px dotted;
}

.scoped-bootstrap b,
.scoped-bootstrap strong {
  font-weight: bold;
}

.scoped-bootstrap dfn {
  font-style: italic;
}

.scoped-bootstrap h1 {
  margin: .67em 0;
  font-size: 2em;
}

.scoped-bootstrap mark {
  color: #000;
  background: #ff0;
}

.scoped-bootstrap small {
  font-size: 80%;
}

.scoped-bootstrap sub,
.scoped-bootstrap sup {
  position: relative;
  font-size: 75%;
  line-height: 0;
  vertical-align: baseline;
}

.scoped-bootstrap sup {
  top: -.5em;
}

.scoped-bootstrap sub {
  bottom: -.25em;
}

.scoped-bootstrap img {
  border: 0;
}

.scoped-bootstrap svg:not(:root) {
  overflow: hidden;
}

.scoped-bootstrap figure {
  margin: 1em 40px;
}

.scoped-bootstrap hr {
  height: 0;
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}

pre {
  overflow: auto;
}

code,
.scoped-bootstrap kbd,
pre,
.scoped-bootstrap samp {
  font-family: monospace, monospace;
  font-size: 1em;
}

.scoped-bootstrap button,
.scoped-bootstrap input,
.scoped-bootstrap optgroup,
.scoped-bootstrap select,
.scoped-bootstrap textarea {
  margin: 0;
  font: inherit;
  color: inherit;
}

.scoped-bootstrap button {
  overflow: visible;
}

.scoped-bootstrap button,
.scoped-bootstrap select {
  text-transform: none;
}

.scoped-bootstrap button,
.scoped-bootstrap input[type="button"],
.scoped-bootstrap input[type="reset"],
.scoped-bootstrap input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}

.scoped-bootstrap button[disabled],
.scoped-bootstrap input[disabled] {
  cursor: default;
}

.scoped-bootstrap button::-moz-focus-inner,
.scoped-bootstrap input::-moz-focus-inner {
  padding: 0;
  border: 0;
}

.scoped-bootstrap input {
  line-height: normal;
}

.scoped-bootstrap input[type="checkbox"],
.scoped-bootstrap input[type="radio"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  padding: 0;
}

.scoped-bootstrap input[type="number"]::-webkit-inner-spin-button,
.scoped-bootstrap input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}

.scoped-bootstrap input[type="search"] {
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  -webkit-appearance: textfield;
}

.scoped-bootstrap input[type="search"]::-webkit-search-cancel-button,
.scoped-bootstrap input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}

.scoped-bootstrap fieldset {
  padding: .35em .625em .75em;
  margin: 0 2px;
  border: 1px solid #c0c0c0;
}

.scoped-bootstrap legend {
  padding: 0;
  border: 0;
}

.scoped-bootstrap textarea {
  overflow: auto;
}

.scoped-bootstrap optgroup {
  font-weight: bold;
}

.scoped-bootstrap table {
  border-spacing: 0;
  border-collapse: collapse;
}

.scoped-bootstrap td,
.scoped-bootstrap th {
  padding: 0;
}

/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */

@media print {
  .scoped-bootstrap *,
  .scoped-bootstrap *:before,
  .scoped-bootstrap *:after {
    color: #000 !important;
    text-shadow: none !important;
    background: transparent !important;
    -webkit-box-shadow: none !important;
    box-shadow: none !important;
  }

  .scoped-bootstrap a,
  .scoped-bootstrap a:visited {
    text-decoration: underline;
  }

  .scoped-bootstrap a[href]:after {
    content: " (" attr(href) ")";
  }

  .scoped-bootstrap abbr[title]:after {
    content: " (" attr(title) ")";
  }

  .scoped-bootstrap a[href^="#"]:after,
  .scoped-bootstrap a[href^="javascript:"]:after {
    content: "";
  }

  pre,
  .scoped-bootstrap blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }

  .scoped-bootstrap thead {
    display: table-header-group;
  }

  .scoped-bootstrap tr,
  .scoped-bootstrap img {
    page-break-inside: avoid;
  }

  .scoped-bootstrap img {
    max-width: 100% !important;
  }

  .scoped-bootstrap p,
  .scoped-bootstrap h2,
  .scoped-bootstrap h3 {
    orphans: 3;
    widows: 3;
  }

  .scoped-bootstrap h2,
  .scoped-bootstrap h3 {
    page-break-after: avoid;
  }

  .scoped-bootstrap .navbar {
    display: none;
  }

  .scoped-bootstrap .btn > .caret,
  .scoped-bootstrap .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }

  .scoped-bootstrap .label {
    border: 1px solid #000;
  }

  .scoped-bootstrap .table {
    border-collapse: collapse !important;
  }

  .scoped-bootstrap .table td,
  .scoped-bootstrap .table th {
    background-color: #fff !important;
  }

  .scoped-bootstrap .table-bordered th,
  .scoped-bootstrap .table-bordered td {
    border: 1px solid #ddd !important;
  }
}

.scoped-bootstrap * {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

.scoped-bootstrap *:before,
.scoped-bootstrap *:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

.scoped-bootstrap {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

.scoped-bootstrap {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  line-height: 1.42857143;
  color: #333;
  background-color: #fff;
}

.scoped-bootstrap input,
.scoped-bootstrap button,
.scoped-bootstrap select,
.scoped-bootstrap textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}

.scoped-bootstrap a {
  color: #337ab7;
  text-decoration: none;
}

.scoped-bootstrap a:hover,
.scoped-bootstrap a:focus {
  color: #23527c;
  text-decoration: underline;
}

.scoped-bootstrap a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}

.scoped-bootstrap figure {
  margin: 0;
}

.scoped-bootstrap img {
  vertical-align: middle;
}

.scoped-bootstrap .img-responsive,
.scoped-bootstrap .thumbnail > img,
.scoped-bootstrap .thumbnail a > img,
.scoped-bootstrap .carousel-inner > .item > img,
.scoped-bootstrap .carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}

.scoped-bootstrap .img-rounded {
  border-radius: 6px;
}

.scoped-bootstrap .img-thumbnail {
  display: inline-block;
  max-width: 100%;
  height: auto;
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  -webkit-transition: all .2s ease-in-out;
  -o-transition: all .2s ease-in-out;
  transition: all .2s ease-in-out;
}

.scoped-bootstrap .img-circle {
  border-radius: 50%;
}

.scoped-bootstrap hr {
  margin-top: 20px;
  margin-bottom: 20px;
  border: 0;
  border-top: 1px solid #eee;
}

.scoped-bootstrap .sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

.scoped-bootstrap .sr-only-focusable:active,
.scoped-bootstrap .sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}

.scoped-bootstrap [role="button"] {
  cursor: pointer;
}

.scoped-bootstrap h1,
.scoped-bootstrap h2,
.scoped-bootstrap h3,
.scoped-bootstrap h4,
.scoped-bootstrap h5,
.scoped-bootstrap h6,
.scoped-bootstrap .h1,
.scoped-bootstrap .h2,
.scoped-bootstrap .h3,
.scoped-bootstrap .h4,
.scoped-bootstrap .h5,
.scoped-bootstrap .h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}

.scoped-bootstrap h1 small,
.scoped-bootstrap h2 small,
.scoped-bootstrap h3 small,
.scoped-bootstrap h4 small,
.scoped-bootstrap h5 small,
.scoped-bootstrap h6 small,
.scoped-bootstrap .h1 small,
.scoped-bootstrap .h2 small,
.scoped-bootstrap .h3 small,
.scoped-bootstrap .h4 small,
.scoped-bootstrap .h5 small,
.scoped-bootstrap .h6 small,
.scoped-bootstrap h1 .small,
.scoped-bootstrap h2 .small,
.scoped-bootstrap h3 .small,
.scoped-bootstrap h4 .small,
.scoped-bootstrap h5 .small,
.scoped-bootstrap h6 .small,
.scoped-bootstrap .h1 .small,
.scoped-bootstrap .h2 .small,
.scoped-bootstrap .h3 .small,
.scoped-bootstrap .h4 .small,
.scoped-bootstrap .h5 .small,
.scoped-bootstrap .h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777;
}

.scoped-bootstrap h1,
.scoped-bootstrap .h1,
.scoped-bootstrap h2,
.scoped-bootstrap .h2,
.scoped-bootstrap h3,
.scoped-bootstrap .h3 {
  margin-top: 20px;
  margin-bottom: 10px;
}

.scoped-bootstrap h1 small,
.scoped-bootstrap .h1 small,
.scoped-bootstrap h2 small,
.scoped-bootstrap .h2 small,
.scoped-bootstrap h3 small,
.scoped-bootstrap .h3 small,
.scoped-bootstrap h1 .small,
.scoped-bootstrap .h1 .small,
.scoped-bootstrap h2 .small,
.scoped-bootstrap .h2 .small,
.scoped-bootstrap h3 .small,
.scoped-bootstrap .h3 .small {
  font-size: 65%;
}

.scoped-bootstrap h4,
.scoped-bootstrap .h4,
.scoped-bootstrap h5,
.scoped-bootstrap .h5,
.scoped-bootstrap h6,
.scoped-bootstrap .h6 {
  margin-top: 10px;
  margin-bottom: 10px;
}

.scoped-bootstrap h4 small,
.scoped-bootstrap .h4 small,
.scoped-bootstrap h5 small,
.scoped-bootstrap .h5 small,
.scoped-bootstrap h6 small,
.scoped-bootstrap .h6 small,
.scoped-bootstrap h4 .small,
.scoped-bootstrap .h4 .small,
.scoped-bootstrap h5 .small,
.scoped-bootstrap .h5 .small,
.scoped-bootstrap h6 .small,
.scoped-bootstrap .h6 .small {
  font-size: 75%;
}

.scoped-bootstrap h1,
.scoped-bootstrap .h1 {
  font-size: 36px;
}

.scoped-bootstrap h2,
.scoped-bootstrap .h2 {
  font-size: 30px;
}

.scoped-bootstrap h3,
.scoped-bootstrap .h3 {
  font-size: 24px;
}

.scoped-bootstrap h4,
.scoped-bootstrap .h4 {
  font-size: 18px;
}

.scoped-bootstrap h5,
.scoped-bootstrap .h5 {
  font-size: 14px;
}

.scoped-bootstrap h6,
.scoped-bootstrap .h6 {
  font-size: 12px;
}

.scoped-bootstrap p {
  margin: 0 0 10px;
}

.scoped-bootstrap .lead {
  margin-bottom: 20px;
  font-size: 16px;
  font-weight: 300;
  line-height: 1.4;
}

@media (min-width: 768px) {
  .scoped-bootstrap .lead {
    font-size: 21px;
  }
}

.scoped-bootstrap small,
.scoped-bootstrap .small {
  font-size: 85%;
}

.scoped-bootstrap mark,
.scoped-bootstrap .mark {
  padding: .2em;
  background-color: #fcf8e3;
}

.scoped-bootstrap .text-left {
  text-align: left;
}

.scoped-bootstrap .text-right {
  text-align: right;
}

.scoped-bootstrap .text-center {
  text-align: center;
}

.scoped-bootstrap .text-justify {
  text-align: justify;
}

.scoped-bootstrap .text-nowrap {
  white-space: nowrap;
}

.scoped-bootstrap .text-lowercase {
  text-transform: lowercase;
}

.scoped-bootstrap .text-uppercase {
  text-transform: uppercase;
}

.scoped-bootstrap .text-capitalize {
  text-transform: capitalize;
}

.scoped-bootstrap .text-muted {
  color: #777;
}

.scoped-bootstrap .text-primary {
  color: #337ab7;
}

.scoped-bootstrap a.text-primary:hover,
.scoped-bootstrap a.text-primary:focus {
  color: #286090;
}

.scoped-bootstrap .text-success {
  color: #3c763d;
}

.scoped-bootstrap a.text-success:hover,
.scoped-bootstrap a.text-success:focus {
  color: #2b542c;
}

.scoped-bootstrap .text-info {
  color: #31708f;
}

.scoped-bootstrap a.text-info:hover,
.scoped-bootstrap a.text-info:focus {
  color: #245269;
}

.scoped-bootstrap .text-warning {
  color: #8a6d3b;
}

.scoped-bootstrap a.text-warning:hover,
.scoped-bootstrap a.text-warning:focus {
  color: #66512c;
}

.scoped-bootstrap .text-danger {
  color: #a94442;
}

.scoped-bootstrap a.text-danger:hover,
.scoped-bootstrap a.text-danger:focus {
  color: #843534;
}

.scoped-bootstrap .bg-primary {
  color: #fff;
  background-color: #337ab7;
}

.scoped-bootstrap a.bg-primary:hover,
.scoped-bootstrap a.bg-primary:focus {
  background-color: #286090;
}

.scoped-bootstrap .bg-success {
  background-color: #dff0d8;
}

.scoped-bootstrap a.bg-success:hover,
.scoped-bootstrap a.bg-success:focus {
  background-color: #c1e2b3;
}

.scoped-bootstrap .bg-info {
  background-color: #d9edf7;
}

.scoped-bootstrap a.bg-info:hover,
.scoped-bootstrap a.bg-info:focus {
  background-color: #afd9ee;
}

.scoped-bootstrap .bg-warning {
  background-color: #fcf8e3;
}

.scoped-bootstrap a.bg-warning:hover,
.scoped-bootstrap a.bg-warning:focus {
  background-color: #f7ecb5;
}

.scoped-bootstrap .bg-danger {
  background-color: #f2dede;
}

.scoped-bootstrap a.bg-danger:hover,
.scoped-bootstrap a.bg-danger:focus {
  background-color: #e4b9b9;
}

.scoped-bootstrap .page-header {
  padding-bottom: 9px;
  margin: 40px 0 20px;
  border-bottom: 1px solid #eee;
}

.scoped-bootstrap ul,
.scoped-bootstrap ol {
  margin-top: 0;
  margin-bottom: 10px;
}

.scoped-bootstrap ul ul,
.scoped-bootstrap ol ul,
.scoped-bootstrap ul ol,
.scoped-bootstrap ol ol {
  margin-bottom: 0;
}

.scoped-bootstrap .list-unstyled {
  padding-left: 0;
  list-style: none;
}

.scoped-bootstrap .list-inline {
  padding-left: 0;
  margin-left: -5px;
  list-style: none;
}

.scoped-bootstrap .list-inline > li {
  display: inline-block;
  padding-right: 5px;
  padding-left: 5px;
}

.scoped-bootstrap dl {
  margin-top: 0;
  margin-bottom: 20px;
}

.scoped-bootstrap dt,
.scoped-bootstrap dd {
  line-height: 1.42857143;
}

.scoped-bootstrap dt {
  font-weight: bold;
}

.scoped-bootstrap dd {
  margin-left: 0;
}

@media (min-width: 768px) {
  .scoped-bootstrap .dl-horizontal dt {
    float: left;
    width: 160px;
    overflow: hidden;
    clear: left;
    text-align: right;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .scoped-bootstrap .dl-horizontal dd {
    margin-left: 180px;
  }
}

.scoped-bootstrap abbr[title],
.scoped-bootstrap abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777;
}

.scoped-bootstrap .initialism {
  font-size: 90%;
  text-transform: uppercase;
}

.scoped-bootstrap blockquote {
  padding: 10px 20px;
  margin: 0 0 20px;
  font-size: 17.5px;
  border-left: 5px solid #eee;
}

.scoped-bootstrap blockquote p:last-child,
.scoped-bootstrap blockquote ul:last-child,
.scoped-bootstrap blockquote ol:last-child {
  margin-bottom: 0;
}

.scoped-bootstrap blockquote footer,
.scoped-bootstrap blockquote small,
.scoped-bootstrap blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777;
}

.scoped-bootstrap blockquote footer:before,
.scoped-bootstrap blockquote small:before,
.scoped-bootstrap blockquote .small:before {
  content: '\2014   \A0';
}

.scoped-bootstrap .blockquote-reverse,
.scoped-bootstrap blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  text-align: right;
  border-right: 5px solid #eee;
  border-left: 0;
}

.scoped-bootstrap .blockquote-reverse footer:before,
.scoped-bootstrap blockquote.pull-right footer:before,
.scoped-bootstrap .blockquote-reverse small:before,
.scoped-bootstrap blockquote.pull-right small:before,
.scoped-bootstrap .blockquote-reverse .small:before,
.scoped-bootstrap blockquote.pull-right .small:before {
  content: '';
}

.scoped-bootstrap .blockquote-reverse footer:after,
.scoped-bootstrap blockquote.pull-right footer:after,
.scoped-bootstrap .blockquote-reverse small:after,
.scoped-bootstrap blockquote.pull-right small:after,
.scoped-bootstrap .blockquote-reverse .small:after,
.scoped-bootstrap blockquote.pull-right .small:after {
  content: '\A0   \2014';
}

.scoped-bootstrap address {
  margin-bottom: 20px;
  font-style: normal;
  line-height: 1.42857143;
}

code,
.scoped-bootstrap kbd,
pre,
.scoped-bootstrap samp {
  font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
}

code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 4px;
}

.scoped-bootstrap kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #fff;
  background-color: #333;
  border-radius: 3px;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, .25);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, .25);
}

.scoped-bootstrap kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  -webkit-box-shadow: none;
  box-shadow: none;
}

pre {
  display: block;
  padding: 9.5px;
  margin: 0 0 10px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #333;
  word-break: break-all;
  word-wrap: break-word;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 4px;
}

pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}

.scoped-bootstrap .pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}

.scoped-bootstrap .container {
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}

@media (min-width: 768px) {
  .scoped-bootstrap .container {
    width: 750px;
  }
}

@media (min-width: 992px) {
  .scoped-bootstrap .container {
    width: 970px;
  }
}

@media (min-width: 1200px) {
  .scoped-bootstrap .container {
    width: 1170px;
  }
}

.scoped-bootstrap .container-fluid {
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}

.scoped-bootstrap .row {
  margin-right: -15px;
  margin-left: -15px;
}

.scoped-bootstrap .col-xs-1,
.scoped-bootstrap .col-sm-1,
.scoped-bootstrap .col-md-1,
.scoped-bootstrap .col-lg-1,
.scoped-bootstrap .col-xs-2,
.scoped-bootstrap .col-sm-2,
.scoped-bootstrap .col-md-2,
.scoped-bootstrap .col-lg-2,
.scoped-bootstrap .col-xs-3,
.scoped-bootstrap .col-sm-3,
.scoped-bootstrap .col-md-3,
.scoped-bootstrap .col-lg-3,
.scoped-bootstrap .col-xs-4,
.scoped-bootstrap .col-sm-4,
.scoped-bootstrap .col-md-4,
.scoped-bootstrap .col-lg-4,
.scoped-bootstrap .col-xs-5,
.scoped-bootstrap .col-sm-5,
.scoped-bootstrap .col-md-5,
.scoped-bootstrap .col-lg-5,
.scoped-bootstrap .col-xs-6,
.scoped-bootstrap .col-sm-6,
.scoped-bootstrap .col-md-6,
.scoped-bootstrap .col-lg-6,
.scoped-bootstrap .col-xs-7,
.scoped-bootstrap .col-sm-7,
.scoped-bootstrap .col-md-7,
.scoped-bootstrap .col-lg-7,
.scoped-bootstrap .col-xs-8,
.scoped-bootstrap .col-sm-8,
.scoped-bootstrap .col-md-8,
.scoped-bootstrap .col-lg-8,
.scoped-bootstrap .col-xs-9,
.scoped-bootstrap .col-sm-9,
.scoped-bootstrap .col-md-9,
.scoped-bootstrap .col-lg-9,
.scoped-bootstrap .col-xs-10,
.scoped-bootstrap .col-sm-10,
.scoped-bootstrap .col-md-10,
.scoped-bootstrap .col-lg-10,
.scoped-bootstrap .col-xs-11,
.scoped-bootstrap .col-sm-11,
.scoped-bootstrap .col-md-11,
.scoped-bootstrap .col-lg-11,
.scoped-bootstrap .col-xs-12,
.scoped-bootstrap .col-sm-12,
.scoped-bootstrap .col-md-12,
.scoped-bootstrap .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-right: 15px;
  padding-left: 15px;
}

.scoped-bootstrap .col-xs-1,
.scoped-bootstrap .col-xs-2,
.scoped-bootstrap .col-xs-3,
.scoped-bootstrap .col-xs-4,
.scoped-bootstrap .col-xs-5,
.scoped-bootstrap .col-xs-6,
.scoped-bootstrap .col-xs-7,
.scoped-bootstrap .col-xs-8,
.scoped-bootstrap .col-xs-9,
.scoped-bootstrap .col-xs-10,
.scoped-bootstrap .col-xs-11,
.scoped-bootstrap .col-xs-12 {
  float: left;
}

.scoped-bootstrap .col-xs-12 {
  width: 100%;
}

.scoped-bootstrap .col-xs-11 {
  width: 91.66666667%;
}

.scoped-bootstrap .col-xs-10 {
  width: 83.33333333%;
}

.scoped-bootstrap .col-xs-9 {
  width: 75%;
}

.scoped-bootstrap .col-xs-8 {
  width: 66.66666667%;
}

.scoped-bootstrap .col-xs-7 {
  width: 58.33333333%;
}

.scoped-bootstrap .col-xs-6 {
  width: 50%;
}

.scoped-bootstrap .col-xs-5 {
  width: 41.66666667%;
}

.scoped-bootstrap .col-xs-4 {
  width: 33.33333333%;
}

.scoped-bootstrap .col-xs-3 {
  width: 25%;
}

.scoped-bootstrap .col-xs-2 {
  width: 16.66666667%;
}

.scoped-bootstrap .col-xs-1 {
  width: 8.33333333%;
}

.scoped-bootstrap .col-xs-pull-12 {
  right: 100%;
}

.scoped-bootstrap .col-xs-pull-11 {
  right: 91.66666667%;
}

.scoped-bootstrap .col-xs-pull-10 {
  right: 83.33333333%;
}

.scoped-bootstrap .col-xs-pull-9 {
  right: 75%;
}

.scoped-bootstrap .col-xs-pull-8 {
  right: 66.66666667%;
}

.scoped-bootstrap .col-xs-pull-7 {
  right: 58.33333333%;
}

.scoped-bootstrap .col-xs-pull-6 {
  right: 50%;
}

.scoped-bootstrap .col-xs-pull-5 {
  right: 41.66666667%;
}

.scoped-bootstrap .col-xs-pull-4 {
  right: 33.33333333%;
}

.scoped-bootstrap .col-xs-pull-3 {
  right: 25%;
}

.scoped-bootstrap .col-xs-pull-2 {
  right: 16.66666667%;
}

.scoped-bootstrap .col-xs-pull-1 {
  right: 8.33333333%;
}

.scoped-bootstrap .col-xs-pull-0 {
  right: auto;
}

.scoped-bootstrap .col-xs-push-12 {
  left: 100%;
}

.scoped-bootstrap .col-xs-push-11 {
  left: 91.66666667%;
}

.scoped-bootstrap .col-xs-push-10 {
  left: 83.33333333%;
}

.scoped-bootstrap .col-xs-push-9 {
  left: 75%;
}

.scoped-bootstrap .col-xs-push-8 {
  left: 66.66666667%;
}

.scoped-bootstrap .col-xs-push-7 {
  left: 58.33333333%;
}

.scoped-bootstrap .col-xs-push-6 {
  left: 50%;
}

.scoped-bootstrap .col-xs-push-5 {
  left: 41.66666667%;
}

.scoped-bootstrap .col-xs-push-4 {
  left: 33.33333333%;
}

.scoped-bootstrap .col-xs-push-3 {
  left: 25%;
}

.scoped-bootstrap .col-xs-push-2 {
  left: 16.66666667%;
}

.scoped-bootstrap .col-xs-push-1 {
  left: 8.33333333%;
}

.scoped-bootstrap .col-xs-push-0 {
  left: auto;
}

.scoped-bootstrap .col-xs-offset-12 {
  margin-left: 100%;
}

.scoped-bootstrap .col-xs-offset-11 {
  margin-left: 91.66666667%;
}

.scoped-bootstrap .col-xs-offset-10 {
  margin-left: 83.33333333%;
}

.scoped-bootstrap .col-xs-offset-9 {
  margin-left: 75%;
}

.scoped-bootstrap .col-xs-offset-8 {
  margin-left: 66.66666667%;
}

.scoped-bootstrap .col-xs-offset-7 {
  margin-left: 58.33333333%;
}

.scoped-bootstrap .col-xs-offset-6 {
  margin-left: 50%;
}

.scoped-bootstrap .col-xs-offset-5 {
  margin-left: 41.66666667%;
}

.scoped-bootstrap .col-xs-offset-4 {
  margin-left: 33.33333333%;
}

.scoped-bootstrap .col-xs-offset-3 {
  margin-left: 25%;
}

.scoped-bootstrap .col-xs-offset-2 {
  margin-left: 16.66666667%;
}

.scoped-bootstrap .col-xs-offset-1 {
  margin-left: 8.33333333%;
}

.scoped-bootstrap .col-xs-offset-0 {
  margin-left: 0;
}

@media (min-width: 768px) {
  .scoped-bootstrap .col-sm-1,
  .scoped-bootstrap .col-sm-2,
  .scoped-bootstrap .col-sm-3,
  .scoped-bootstrap .col-sm-4,
  .scoped-bootstrap .col-sm-5,
  .scoped-bootstrap .col-sm-6,
  .scoped-bootstrap .col-sm-7,
  .scoped-bootstrap .col-sm-8,
  .scoped-bootstrap .col-sm-9,
  .scoped-bootstrap .col-sm-10,
  .scoped-bootstrap .col-sm-11,
  .scoped-bootstrap .col-sm-12 {
    float: left;
  }

  .scoped-bootstrap .col-sm-12 {
    width: 100%;
  }

  .scoped-bootstrap .col-sm-11 {
    width: 91.66666667%;
  }

  .scoped-bootstrap .col-sm-10 {
    width: 83.33333333%;
  }

  .scoped-bootstrap .col-sm-9 {
    width: 75%;
  }

  .scoped-bootstrap .col-sm-8 {
    width: 66.66666667%;
  }

  .scoped-bootstrap .col-sm-7 {
    width: 58.33333333%;
  }

  .scoped-bootstrap .col-sm-6 {
    width: 50%;
  }

  .scoped-bootstrap .col-sm-5 {
    width: 41.66666667%;
  }

  .scoped-bootstrap .col-sm-4 {
    width: 33.33333333%;
  }

  .scoped-bootstrap .col-sm-3 {
    width: 25%;
  }

  .scoped-bootstrap .col-sm-2 {
    width: 16.66666667%;
  }

  .scoped-bootstrap .col-sm-1 {
    width: 8.33333333%;
  }

  .scoped-bootstrap .col-sm-pull-12 {
    right: 100%;
  }

  .scoped-bootstrap .col-sm-pull-11 {
    right: 91.66666667%;
  }

  .scoped-bootstrap .col-sm-pull-10 {
    right: 83.33333333%;
  }

  .scoped-bootstrap .col-sm-pull-9 {
    right: 75%;
  }

  .scoped-bootstrap .col-sm-pull-8 {
    right: 66.66666667%;
  }

  .scoped-bootstrap .col-sm-pull-7 {
    right: 58.33333333%;
  }

  .scoped-bootstrap .col-sm-pull-6 {
    right: 50%;
  }

  .scoped-bootstrap .col-sm-pull-5 {
    right: 41.66666667%;
  }

  .scoped-bootstrap .col-sm-pull-4 {
    right: 33.33333333%;
  }

  .scoped-bootstrap .col-sm-pull-3 {
    right: 25%;
  }

  .scoped-bootstrap .col-sm-pull-2 {
    right: 16.66666667%;
  }

  .scoped-bootstrap .col-sm-pull-1 {
    right: 8.33333333%;
  }

  .scoped-bootstrap .col-sm-pull-0 {
    right: auto;
  }

  .scoped-bootstrap .col-sm-push-12 {
    left: 100%;
  }

  .scoped-bootstrap .col-sm-push-11 {
    left: 91.66666667%;
  }

  .scoped-bootstrap .col-sm-push-10 {
    left: 83.33333333%;
  }

  .scoped-bootstrap .col-sm-push-9 {
    left: 75%;
  }

  .scoped-bootstrap .col-sm-push-8 {
    left: 66.66666667%;
  }

  .scoped-bootstrap .col-sm-push-7 {
    left: 58.33333333%;
  }

  .scoped-bootstrap .col-sm-push-6 {
    left: 50%;
  }

  .scoped-bootstrap .col-sm-push-5 {
    left: 41.66666667%;
  }

  .scoped-bootstrap .col-sm-push-4 {
    left: 33.33333333%;
  }

  .scoped-bootstrap .col-sm-push-3 {
    left: 25%;
  }

  .scoped-bootstrap .col-sm-push-2 {
    left: 16.66666667%;
  }

  .scoped-bootstrap .col-sm-push-1 {
    left: 8.33333333%;
  }

  .scoped-bootstrap .col-sm-push-0 {
    left: auto;
  }

  .scoped-bootstrap .col-sm-offset-12 {
    margin-left: 100%;
  }

  .scoped-bootstrap .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }

  .scoped-bootstrap .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }

  .scoped-bootstrap .col-sm-offset-9 {
    margin-left: 75%;
  }

  .scoped-bootstrap .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }

  .scoped-bootstrap .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }

  .scoped-bootstrap .col-sm-offset-6 {
    margin-left: 50%;
  }

  .scoped-bootstrap .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }

  .scoped-bootstrap .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }

  .scoped-bootstrap .col-sm-offset-3 {
    margin-left: 25%;
  }

  .scoped-bootstrap .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }

  .scoped-bootstrap .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }

  .scoped-bootstrap .col-sm-offset-0 {
    margin-left: 0;
  }
}

@media (min-width: 992px) {
  .scoped-bootstrap .col-md-1,
  .scoped-bootstrap .col-md-2,
  .scoped-bootstrap .col-md-3,
  .scoped-bootstrap .col-md-4,
  .scoped-bootstrap .col-md-5,
  .scoped-bootstrap .col-md-6,
  .scoped-bootstrap .col-md-7,
  .scoped-bootstrap .col-md-8,
  .scoped-bootstrap .col-md-9,
  .scoped-bootstrap .col-md-10,
  .scoped-bootstrap .col-md-11,
  .scoped-bootstrap .col-md-12 {
    float: left;
  }

  .scoped-bootstrap .col-md-12 {
    width: 100%;
  }

  .scoped-bootstrap .col-md-11 {
    width: 91.66666667%;
  }

  .scoped-bootstrap .col-md-10 {
    width: 83.33333333%;
  }

  .scoped-bootstrap .col-md-9 {
    width: 75%;
  }

  .scoped-bootstrap .col-md-8 {
    width: 66.66666667%;
  }

  .scoped-bootstrap .col-md-7 {
    width: 58.33333333%;
  }

  .scoped-bootstrap .col-md-6 {
    width: 50%;
  }

  .scoped-bootstrap .col-md-5 {
    width: 41.66666667%;
  }

  .scoped-bootstrap .col-md-4 {
    width: 33.33333333%;
  }

  .scoped-bootstrap .col-md-3 {
    width: 25%;
  }

  .scoped-bootstrap .col-md-2 {
    width: 16.66666667%;
  }

  .scoped-bootstrap .col-md-1 {
    width: 8.33333333%;
  }

  .scoped-bootstrap .col-md-pull-12 {
    right: 100%;
  }

  .scoped-bootstrap .col-md-pull-11 {
    right: 91.66666667%;
  }

  .scoped-bootstrap .col-md-pull-10 {
    right: 83.33333333%;
  }

  .scoped-bootstrap .col-md-pull-9 {
    right: 75%;
  }

  .scoped-bootstrap .col-md-pull-8 {
    right: 66.66666667%;
  }

  .scoped-bootstrap .col-md-pull-7 {
    right: 58.33333333%;
  }

  .scoped-bootstrap .col-md-pull-6 {
    right: 50%;
  }

  .scoped-bootstrap .col-md-pull-5 {
    right: 41.66666667%;
  }

  .scoped-bootstrap .col-md-pull-4 {
    right: 33.33333333%;
  }

  .scoped-bootstrap .col-md-pull-3 {
    right: 25%;
  }

  .scoped-bootstrap .col-md-pull-2 {
    right: 16.66666667%;
  }

  .scoped-bootstrap .col-md-pull-1 {
    right: 8.33333333%;
  }

  .scoped-bootstrap .col-md-pull-0 {
    right: auto;
  }

  .scoped-bootstrap .col-md-push-12 {
    left: 100%;
  }

  .scoped-bootstrap .col-md-push-11 {
    left: 91.66666667%;
  }

  .scoped-bootstrap .col-md-push-10 {
    left: 83.33333333%;
  }

  .scoped-bootstrap .col-md-push-9 {
    left: 75%;
  }

  .scoped-bootstrap .col-md-push-8 {
    left: 66.66666667%;
  }

  .scoped-bootstrap .col-md-push-7 {
    left: 58.33333333%;
  }

  .scoped-bootstrap .col-md-push-6 {
    left: 50%;
  }

  .scoped-bootstrap .col-md-push-5 {
    left: 41.66666667%;
  }

  .scoped-bootstrap .col-md-push-4 {
    left: 33.33333333%;
  }

  .scoped-bootstrap .col-md-push-3 {
    left: 25%;
  }

  .scoped-bootstrap .col-md-push-2 {
    left: 16.66666667%;
  }

  .scoped-bootstrap .col-md-push-1 {
    left: 8.33333333%;
  }

  .scoped-bootstrap .col-md-push-0 {
    left: auto;
  }

  .scoped-bootstrap .col-md-offset-12 {
    margin-left: 100%;
  }

  .scoped-bootstrap .col-md-offset-11 {
    margin-left: 91.66666667%;
  }

  .scoped-bootstrap .col-md-offset-10 {
    margin-left: 83.33333333%;
  }

  .scoped-bootstrap .col-md-offset-9 {
    margin-left: 75%;
  }

  .scoped-bootstrap .col-md-offset-8 {
    margin-left: 66.66666667%;
  }

  .scoped-bootstrap .col-md-offset-7 {
    margin-left: 58.33333333%;
  }

  .scoped-bootstrap .col-md-offset-6 {
    margin-left: 50%;
  }

  .scoped-bootstrap .col-md-offset-5 {
    margin-left: 41.66666667%;
  }

  .scoped-bootstrap .col-md-offset-4 {
    margin-left: 33.33333333%;
  }

  .scoped-bootstrap .col-md-offset-3 {
    margin-left: 25%;
  }

  .scoped-bootstrap .col-md-offset-2 {
    margin-left: 16.66666667%;
  }

  .scoped-bootstrap .col-md-offset-1 {
    margin-left: 8.33333333%;
  }

  .scoped-bootstrap .col-md-offset-0 {
    margin-left: 0;
  }
}

@media (min-width: 1200px) {
  .scoped-bootstrap .col-lg-1,
  .scoped-bootstrap .col-lg-2,
  .scoped-bootstrap .col-lg-3,
  .scoped-bootstrap .col-lg-4,
  .scoped-bootstrap .col-lg-5,
  .scoped-bootstrap .col-lg-6,
  .scoped-bootstrap .col-lg-7,
  .scoped-bootstrap .col-lg-8,
  .scoped-bootstrap .col-lg-9,
  .scoped-bootstrap .col-lg-10,
  .scoped-bootstrap .col-lg-11,
  .scoped-bootstrap .col-lg-12 {
    float: left;
  }

  .scoped-bootstrap .col-lg-12 {
    width: 100%;
  }

  .scoped-bootstrap .col-lg-11 {
    width: 91.66666667%;
  }

  .scoped-bootstrap .col-lg-10 {
    width: 83.33333333%;
  }

  .scoped-bootstrap .col-lg-9 {
    width: 75%;
  }

  .scoped-bootstrap .col-lg-8 {
    width: 66.66666667%;
  }

  .scoped-bootstrap .col-lg-7 {
    width: 58.33333333%;
  }

  .scoped-bootstrap .col-lg-6 {
    width: 50%;
  }

  .scoped-bootstrap .col-lg-5 {
    width: 41.66666667%;
  }

  .scoped-bootstrap .col-lg-4 {
    width: 33.33333333%;
  }

  .scoped-bootstrap .col-lg-3 {
    width: 25%;
  }

  .scoped-bootstrap .col-lg-2 {
    width: 16.66666667%;
  }

  .scoped-bootstrap .col-lg-1 {
    width: 8.33333333%;
  }

  .scoped-bootstrap .col-lg-pull-12 {
    right: 100%;
  }

  .scoped-bootstrap .col-lg-pull-11 {
    right: 91.66666667%;
  }

  .scoped-bootstrap .col-lg-pull-10 {
    right: 83.33333333%;
  }

  .scoped-bootstrap .col-lg-pull-9 {
    right: 75%;
  }

  .scoped-bootstrap .col-lg-pull-8 {
    right: 66.66666667%;
  }

  .scoped-bootstrap .col-lg-pull-7 {
    right: 58.33333333%;
  }

  .scoped-bootstrap .col-lg-pull-6 {
    right: 50%;
  }

  .scoped-bootstrap .col-lg-pull-5 {
    right: 41.66666667%;
  }

  .scoped-bootstrap .col-lg-pull-4 {
    right: 33.33333333%;
  }

  .scoped-bootstrap .col-lg-pull-3 {
    right: 25%;
  }

  .scoped-bootstrap .col-lg-pull-2 {
    right: 16.66666667%;
  }

  .scoped-bootstrap .col-lg-pull-1 {
    right: 8.33333333%;
  }

  .scoped-bootstrap .col-lg-pull-0 {
    right: auto;
  }

  .scoped-bootstrap .col-lg-push-12 {
    left: 100%;
  }

  .scoped-bootstrap .col-lg-push-11 {
    left: 91.66666667%;
  }

  .scoped-bootstrap .col-lg-push-10 {
    left: 83.33333333%;
  }

  .scoped-bootstrap .col-lg-push-9 {
    left: 75%;
  }

  .scoped-bootstrap .col-lg-push-8 {
    left: 66.66666667%;
  }

  .scoped-bootstrap .col-lg-push-7 {
    left: 58.33333333%;
  }

  .scoped-bootstrap .col-lg-push-6 {
    left: 50%;
  }

  .scoped-bootstrap .col-lg-push-5 {
    left: 41.66666667%;
  }

  .scoped-bootstrap .col-lg-push-4 {
    left: 33.33333333%;
  }

  .scoped-bootstrap .col-lg-push-3 {
    left: 25%;
  }

  .scoped-bootstrap .col-lg-push-2 {
    left: 16.66666667%;
  }

  .scoped-bootstrap .col-lg-push-1 {
    left: 8.33333333%;
  }

  .scoped-bootstrap .col-lg-push-0 {
    left: auto;
  }

  .scoped-bootstrap .col-lg-offset-12 {
    margin-left: 100%;
  }

  .scoped-bootstrap .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }

  .scoped-bootstrap .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }

  .scoped-bootstrap .col-lg-offset-9 {
    margin-left: 75%;
  }

  .scoped-bootstrap .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }

  .scoped-bootstrap .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }

  .scoped-bootstrap .col-lg-offset-6 {
    margin-left: 50%;
  }

  .scoped-bootstrap .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }

  .scoped-bootstrap .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }

  .scoped-bootstrap .col-lg-offset-3 {
    margin-left: 25%;
  }

  .scoped-bootstrap .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }

  .scoped-bootstrap .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }

  .scoped-bootstrap .col-lg-offset-0 {
    margin-left: 0;
  }
}

.scoped-bootstrap table {
  background-color: transparent;
}

.scoped-bootstrap caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777;
  text-align: left;
}

.scoped-bootstrap th {
  text-align: left;
}

.scoped-bootstrap .table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 20px;
}

.scoped-bootstrap .table > thead > tr > th,
.scoped-bootstrap .table > tbody > tr > th,
.scoped-bootstrap .table > tfoot > tr > th,
.scoped-bootstrap .table > thead > tr > td,
.scoped-bootstrap .table > tbody > tr > td,
.scoped-bootstrap .table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}

.scoped-bootstrap .table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}

.scoped-bootstrap .table > caption + thead > tr:first-child > th,
.scoped-bootstrap .table > colgroup + thead > tr:first-child > th,
.scoped-bootstrap .table > thead:first-child > tr:first-child > th,
.scoped-bootstrap .table > caption + thead > tr:first-child > td,
.scoped-bootstrap .table > colgroup + thead > tr:first-child > td,
.scoped-bootstrap .table > thead:first-child > tr:first-child > td {
  border-top: 0;
}

.scoped-bootstrap .table > tbody + tbody {
  border-top: 2px solid #ddd;
}

.scoped-bootstrap .table .table {
  background-color: #fff;
}

.scoped-bootstrap .table-condensed > thead > tr > th,
.scoped-bootstrap .table-condensed > tbody > tr > th,
.scoped-bootstrap .table-condensed > tfoot > tr > th,
.scoped-bootstrap .table-condensed > thead > tr > td,
.scoped-bootstrap .table-condensed > tbody > tr > td,
.scoped-bootstrap .table-condensed > tfoot > tr > td {
  padding: 5px;
}

.scoped-bootstrap .table-bordered {
  border: 1px solid #ddd;
}

.scoped-bootstrap .table-bordered > thead > tr > th,
.scoped-bootstrap .table-bordered > tbody > tr > th,
.scoped-bootstrap .table-bordered > tfoot > tr > th,
.scoped-bootstrap .table-bordered > thead > tr > td,
.scoped-bootstrap .table-bordered > tbody > tr > td,
.scoped-bootstrap .table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}

.scoped-bootstrap .table-bordered > thead > tr > th,
.scoped-bootstrap .table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}

.scoped-bootstrap .table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}

.scoped-bootstrap .table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}

.scoped-bootstrap table col[class*="col-"] {
  position: static;
  display: table-column;
  float: none;
}

.scoped-bootstrap table td[class*="col-"],
.scoped-bootstrap table th[class*="col-"] {
  position: static;
  display: table-cell;
  float: none;
}

.scoped-bootstrap .table > thead > tr > td.active,
.scoped-bootstrap .table > tbody > tr > td.active,
.scoped-bootstrap .table > tfoot > tr > td.active,
.scoped-bootstrap .table > thead > tr > th.active,
.scoped-bootstrap .table > tbody > tr > th.active,
.scoped-bootstrap .table > tfoot > tr > th.active,
.scoped-bootstrap .table > thead > tr.active > td,
.scoped-bootstrap .table > tbody > tr.active > td,
.scoped-bootstrap .table > tfoot > tr.active > td,
.scoped-bootstrap .table > thead > tr.active > th,
.scoped-bootstrap .table > tbody > tr.active > th,
.scoped-bootstrap .table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}

.scoped-bootstrap .table-hover > tbody > tr > td.active:hover,
.scoped-bootstrap .table-hover > tbody > tr > th.active:hover,
.scoped-bootstrap .table-hover > tbody > tr.active:hover > td,
.scoped-bootstrap .table-hover > tbody > tr:hover > .active,
.scoped-bootstrap .table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}

.scoped-bootstrap .table > thead > tr > td.success,
.scoped-bootstrap .table > tbody > tr > td.success,
.scoped-bootstrap .table > tfoot > tr > td.success,
.scoped-bootstrap .table > thead > tr > th.success,
.scoped-bootstrap .table > tbody > tr > th.success,
.scoped-bootstrap .table > tfoot > tr > th.success,
.scoped-bootstrap .table > thead > tr.success > td,
.scoped-bootstrap .table > tbody > tr.success > td,
.scoped-bootstrap .table > tfoot > tr.success > td,
.scoped-bootstrap .table > thead > tr.success > th,
.scoped-bootstrap .table > tbody > tr.success > th,
.scoped-bootstrap .table > tfoot > tr.success > th {
  background-color: #dff0d8;
}

.scoped-bootstrap .table-hover > tbody > tr > td.success:hover,
.scoped-bootstrap .table-hover > tbody > tr > th.success:hover,
.scoped-bootstrap .table-hover > tbody > tr.success:hover > td,
.scoped-bootstrap .table-hover > tbody > tr:hover > .success,
.scoped-bootstrap .table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}

.scoped-bootstrap .table > thead > tr > td.info,
.scoped-bootstrap .table > tbody > tr > td.info,
.scoped-bootstrap .table > tfoot > tr > td.info,
.scoped-bootstrap .table > thead > tr > th.info,
.scoped-bootstrap .table > tbody > tr > th.info,
.scoped-bootstrap .table > tfoot > tr > th.info,
.scoped-bootstrap .table > thead > tr.info > td,
.scoped-bootstrap .table > tbody > tr.info > td,
.scoped-bootstrap .table > tfoot > tr.info > td,
.scoped-bootstrap .table > thead > tr.info > th,
.scoped-bootstrap .table > tbody > tr.info > th,
.scoped-bootstrap .table > tfoot > tr.info > th {
  background-color: #d9edf7;
}

.scoped-bootstrap .table-hover > tbody > tr > td.info:hover,
.scoped-bootstrap .table-hover > tbody > tr > th.info:hover,
.scoped-bootstrap .table-hover > tbody > tr.info:hover > td,
.scoped-bootstrap .table-hover > tbody > tr:hover > .info,
.scoped-bootstrap .table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}

.scoped-bootstrap .table > thead > tr > td.warning,
.scoped-bootstrap .table > tbody > tr > td.warning,
.scoped-bootstrap .table > tfoot > tr > td.warning,
.scoped-bootstrap .table > thead > tr > th.warning,
.scoped-bootstrap .table > tbody > tr > th.warning,
.scoped-bootstrap .table > tfoot > tr > th.warning,
.scoped-bootstrap .table > thead > tr.warning > td,
.scoped-bootstrap .table > tbody > tr.warning > td,
.scoped-bootstrap .table > tfoot > tr.warning > td,
.scoped-bootstrap .table > thead > tr.warning > th,
.scoped-bootstrap .table > tbody > tr.warning > th,
.scoped-bootstrap .table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}

.scoped-bootstrap .table-hover > tbody > tr > td.warning:hover,
.scoped-bootstrap .table-hover > tbody > tr > th.warning:hover,
.scoped-bootstrap .table-hover > tbody > tr.warning:hover > td,
.scoped-bootstrap .table-hover > tbody > tr:hover > .warning,
.scoped-bootstrap .table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}

.scoped-bootstrap .table > thead > tr > td.danger,
.scoped-bootstrap .table > tbody > tr > td.danger,
.scoped-bootstrap .table > tfoot > tr > td.danger,
.scoped-bootstrap .table > thead > tr > th.danger,
.scoped-bootstrap .table > tbody > tr > th.danger,
.scoped-bootstrap .table > tfoot > tr > th.danger,
.scoped-bootstrap .table > thead > tr.danger > td,
.scoped-bootstrap .table > tbody > tr.danger > td,
.scoped-bootstrap .table > tfoot > tr.danger > td,
.scoped-bootstrap .table > thead > tr.danger > th,
.scoped-bootstrap .table > tbody > tr.danger > th,
.scoped-bootstrap .table > tfoot > tr.danger > th {
  background-color: #f2dede;
}

.scoped-bootstrap .table-hover > tbody > tr > td.danger:hover,
.scoped-bootstrap .table-hover > tbody > tr > th.danger:hover,
.scoped-bootstrap .table-hover > tbody > tr.danger:hover > td,
.scoped-bootstrap .table-hover > tbody > tr:hover > .danger,
.scoped-bootstrap .table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}

.scoped-bootstrap .table-responsive {
  min-height: .01%;
  overflow-x: auto;
}

@media screen and (max-width: 767px) {
  .scoped-bootstrap .table-responsive {
    width: 100%;
    margin-bottom: 15px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }

  .scoped-bootstrap .table-responsive > .table {
    margin-bottom: 0;
  }

  .scoped-bootstrap .table-responsive > .table > thead > tr > th,
  .scoped-bootstrap .table-responsive > .table > tbody > tr > th,
  .scoped-bootstrap .table-responsive > .table > tfoot > tr > th,
  .scoped-bootstrap .table-responsive > .table > thead > tr > td,
  .scoped-bootstrap .table-responsive > .table > tbody > tr > td,
  .scoped-bootstrap .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }

  .scoped-bootstrap .table-responsive > .table-bordered {
    border: 0;
  }

  .scoped-bootstrap .table-responsive > .table-bordered > thead > tr > th:first-child,
  .scoped-bootstrap .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .scoped-bootstrap .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .scoped-bootstrap .table-responsive > .table-bordered > thead > tr > td:first-child,
  .scoped-bootstrap .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .scoped-bootstrap .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }

  .scoped-bootstrap .table-responsive > .table-bordered > thead > tr > th:last-child,
  .scoped-bootstrap .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .scoped-bootstrap .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .scoped-bootstrap .table-responsive > .table-bordered > thead > tr > td:last-child,
  .scoped-bootstrap .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .scoped-bootstrap .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }

  .scoped-bootstrap .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .scoped-bootstrap .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .scoped-bootstrap .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .scoped-bootstrap .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}

.scoped-bootstrap fieldset {
  min-width: 0;
  padding: 0;
  margin: 0;
  border: 0;
}

.scoped-bootstrap legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 20px;
  font-size: 21px;
  line-height: inherit;
  color: #333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}

.scoped-bootstrap label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}

.scoped-bootstrap input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

.scoped-bootstrap input[type="radio"],
.scoped-bootstrap input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}

.scoped-bootstrap input[type="file"] {
  display: block;
}

.scoped-bootstrap input[type="range"] {
  display: block;
  width: 100%;
}

.scoped-bootstrap select[multiple],
.scoped-bootstrap select[size] {
  height: auto;
}

.scoped-bootstrap input[type="file"]:focus,
.scoped-bootstrap input[type="radio"]:focus,
.scoped-bootstrap input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}

.scoped-bootstrap output {
  display: block;
  padding-top: 7px;
  font-size: 14px;
  line-height: 1.42857143;
  color: #555;
}

.scoped-bootstrap .form-control {
  display: block;
  width: 100%;
  height: 34px;
  padding: 6px 12px;
  font-size: 14px;
  line-height: 1.42857143;
  color: #555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 4px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
  -webkit-transition: border-color ease-in-out .15s, -webkit-box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}

.scoped-bootstrap .form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, .6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, .6);
}

.scoped-bootstrap .form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}

.scoped-bootstrap .form-control:-ms-input-placeholder {
  color: #999;
}

.scoped-bootstrap .form-control::-webkit-input-placeholder {
  color: #999;
}

.scoped-bootstrap .form-control::-ms-expand {
  background-color: transparent;
  border: 0;
}

.scoped-bootstrap .form-control[disabled],
.scoped-bootstrap .form-control[readonly],
.scoped-bootstrap fieldset[disabled] .form-control {
  background-color: #eee;
  opacity: 1;
}

.scoped-bootstrap .form-control[disabled],
.scoped-bootstrap fieldset[disabled] .form-control {
  cursor: not-allowed;
}

.scoped-bootstrap textarea.form-control {
  height: auto;
}

.scoped-bootstrap input[type="search"] {
  -webkit-appearance: none;
}

@media screen and (-webkit-min-device-pixel-ratio: 0) {
  .scoped-bootstrap input[type="date"].form-control,
  .scoped-bootstrap input[type="time"].form-control,
  .scoped-bootstrap input[type="datetime-local"].form-control,
  .scoped-bootstrap input[type="month"].form-control {
    line-height: 34px;
  }

  .scoped-bootstrap input[type="date"].input-sm,
  .scoped-bootstrap input[type="time"].input-sm,
  .scoped-bootstrap input[type="datetime-local"].input-sm,
  .scoped-bootstrap input[type="month"].input-sm,
  .scoped-bootstrap .input-group-sm input[type="date"],
  .scoped-bootstrap .input-group-sm input[type="time"],
  .scoped-bootstrap .input-group-sm input[type="datetime-local"],
  .scoped-bootstrap .input-group-sm input[type="month"] {
    line-height: 30px;
  }

  .scoped-bootstrap input[type="date"].input-lg,
  .scoped-bootstrap input[type="time"].input-lg,
  .scoped-bootstrap input[type="datetime-local"].input-lg,
  .scoped-bootstrap input[type="month"].input-lg,
  .scoped-bootstrap .input-group-lg input[type="date"],
  .scoped-bootstrap .input-group-lg input[type="time"],
  .scoped-bootstrap .input-group-lg input[type="datetime-local"],
  .scoped-bootstrap .input-group-lg input[type="month"] {
    line-height: 46px;
  }
}

.scoped-bootstrap .form-group {
  margin-bottom: 15px;
}

.scoped-bootstrap .radio,
.scoped-bootstrap .checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}

.scoped-bootstrap .radio label,
.scoped-bootstrap .checkbox label {
  min-height: 20px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}

.scoped-bootstrap .radio input[type="radio"],
.scoped-bootstrap .radio-inline input[type="radio"],
.scoped-bootstrap .checkbox input[type="checkbox"],
.scoped-bootstrap .checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-top: 4px \9;
  margin-left: -20px;
}

.scoped-bootstrap .radio + .radio,
.scoped-bootstrap .checkbox + .checkbox {
  margin-top: -5px;
}

.scoped-bootstrap .radio-inline,
.scoped-bootstrap .checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  vertical-align: middle;
  cursor: pointer;
}

.scoped-bootstrap .radio-inline + .radio-inline,
.scoped-bootstrap .checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}

.scoped-bootstrap input[type="radio"][disabled],
.scoped-bootstrap input[type="checkbox"][disabled],
.scoped-bootstrap input[type="radio"].disabled,
.scoped-bootstrap input[type="checkbox"].disabled,
.scoped-bootstrap fieldset[disabled] input[type="radio"],
.scoped-bootstrap fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}

.scoped-bootstrap .radio-inline.disabled,
.scoped-bootstrap .checkbox-inline.disabled,
.scoped-bootstrap fieldset[disabled] .radio-inline,
.scoped-bootstrap fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}

.scoped-bootstrap .radio.disabled label,
.scoped-bootstrap .checkbox.disabled label,
.scoped-bootstrap fieldset[disabled] .radio label,
.scoped-bootstrap fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}

.scoped-bootstrap .form-control-static {
  min-height: 34px;
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
}

.scoped-bootstrap .form-control-static.input-lg,
.scoped-bootstrap .form-control-static.input-sm {
  padding-right: 0;
  padding-left: 0;
}

.scoped-bootstrap .input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 3px;
}

.scoped-bootstrap select.input-sm {
  height: 30px;
  line-height: 30px;
}

.scoped-bootstrap textarea.input-sm,
.scoped-bootstrap select[multiple].input-sm {
  height: auto;
}

.scoped-bootstrap .form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 3px;
}

.scoped-bootstrap .form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}

.scoped-bootstrap .form-group-sm textarea.form-control,
.scoped-bootstrap .form-group-sm select[multiple].form-control {
  height: auto;
}

.scoped-bootstrap .form-group-sm .form-control-static {
  height: 30px;
  min-height: 32px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}

.scoped-bootstrap .input-lg {
  height: 46px;
  padding: 10px 16px;
  font-size: 18px;
  line-height: 1.3333333;
  border-radius: 6px;
}

.scoped-bootstrap select.input-lg {
  height: 46px;
  line-height: 46px;
}

.scoped-bootstrap textarea.input-lg,
.scoped-bootstrap select[multiple].input-lg {
  height: auto;
}

.scoped-bootstrap .form-group-lg .form-control {
  height: 46px;
  padding: 10px 16px;
  font-size: 18px;
  line-height: 1.3333333;
  border-radius: 6px;
}

.scoped-bootstrap .form-group-lg select.form-control {
  height: 46px;
  line-height: 46px;
}

.scoped-bootstrap .form-group-lg textarea.form-control,
.scoped-bootstrap .form-group-lg select[multiple].form-control {
  height: auto;
}

.scoped-bootstrap .form-group-lg .form-control-static {
  height: 46px;
  min-height: 38px;
  padding: 11px 16px;
  font-size: 18px;
  line-height: 1.3333333;
}

.scoped-bootstrap .has-feedback {
  position: relative;
}

.scoped-bootstrap .has-feedback .form-control {
  padding-right: 42.5px;
}

.scoped-bootstrap .form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 34px;
  height: 34px;
  line-height: 34px;
  text-align: center;
  pointer-events: none;
}

.scoped-bootstrap .input-lg + .form-control-feedback,
.scoped-bootstrap .input-group-lg + .form-control-feedback,
.scoped-bootstrap .form-group-lg .form-control + .form-control-feedback {
  width: 46px;
  height: 46px;
  line-height: 46px;
}

.scoped-bootstrap .input-sm + .form-control-feedback,
.scoped-bootstrap .input-group-sm + .form-control-feedback,
.scoped-bootstrap .form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}

.scoped-bootstrap .has-success .help-block,
.scoped-bootstrap .has-success .control-label,
.scoped-bootstrap .has-success .radio,
.scoped-bootstrap .has-success .checkbox,
.scoped-bootstrap .has-success .radio-inline,
.scoped-bootstrap .has-success .checkbox-inline,
.scoped-bootstrap .has-success.radio label,
.scoped-bootstrap .has-success.checkbox label,
.scoped-bootstrap .has-success.radio-inline label,
.scoped-bootstrap .has-success.checkbox-inline label {
  color: #3c763d;
}

.scoped-bootstrap .has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
}

.scoped-bootstrap .has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075), 0 0 6px #67b168;
}

.scoped-bootstrap .has-success .input-group-addon {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #3c763d;
}

.scoped-bootstrap .has-success .form-control-feedback {
  color: #3c763d;
}

.scoped-bootstrap .has-warning .help-block,
.scoped-bootstrap .has-warning .control-label,
.scoped-bootstrap .has-warning .radio,
.scoped-bootstrap .has-warning .checkbox,
.scoped-bootstrap .has-warning .radio-inline,
.scoped-bootstrap .has-warning .checkbox-inline,
.scoped-bootstrap .has-warning.radio label,
.scoped-bootstrap .has-warning.checkbox label,
.scoped-bootstrap .has-warning.radio-inline label,
.scoped-bootstrap .has-warning.checkbox-inline label {
  color: #8a6d3b;
}

.scoped-bootstrap .has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
}

.scoped-bootstrap .has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075), 0 0 6px #c0a16b;
}

.scoped-bootstrap .has-warning .input-group-addon {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #8a6d3b;
}

.scoped-bootstrap .has-warning .form-control-feedback {
  color: #8a6d3b;
}

.scoped-bootstrap .has-error .help-block,
.scoped-bootstrap .has-error .control-label,
.scoped-bootstrap .has-error .radio,
.scoped-bootstrap .has-error .checkbox,
.scoped-bootstrap .has-error .radio-inline,
.scoped-bootstrap .has-error .checkbox-inline,
.scoped-bootstrap .has-error.radio label,
.scoped-bootstrap .has-error.checkbox label,
.scoped-bootstrap .has-error.radio-inline label,
.scoped-bootstrap .has-error.checkbox-inline label {
  color: #a94442;
}

.scoped-bootstrap .has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
}

.scoped-bootstrap .has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075), 0 0 6px #ce8483;
}

.scoped-bootstrap .has-error .input-group-addon {
  color: #a94442;
  background-color: #f2dede;
  border-color: #a94442;
}

.scoped-bootstrap .has-error .form-control-feedback {
  color: #a94442;
}

.scoped-bootstrap .has-feedback label ~ .form-control-feedback {
  top: 25px;
}

.scoped-bootstrap .has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}

.scoped-bootstrap .help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #737373;
}

@media (min-width: 768px) {
  .scoped-bootstrap .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }

  .scoped-bootstrap .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }

  .scoped-bootstrap .form-inline .form-control-static {
    display: inline-block;
  }

  .scoped-bootstrap .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }

  .scoped-bootstrap .form-inline .input-group .input-group-addon,
  .scoped-bootstrap .form-inline .input-group .input-group-btn,
  .scoped-bootstrap .form-inline .input-group .form-control {
    width: auto;
  }

  .scoped-bootstrap .form-inline .input-group > .form-control {
    width: 100%;
  }

  .scoped-bootstrap .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }

  .scoped-bootstrap .form-inline .radio,
  .scoped-bootstrap .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }

  .scoped-bootstrap .form-inline .radio label,
  .scoped-bootstrap .form-inline .checkbox label {
    padding-left: 0;
  }

  .scoped-bootstrap .form-inline .radio input[type="radio"],
  .scoped-bootstrap .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }

  .scoped-bootstrap .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}

.scoped-bootstrap .form-horizontal .radio,
.scoped-bootstrap .form-horizontal .checkbox,
.scoped-bootstrap .form-horizontal .radio-inline,
.scoped-bootstrap .form-horizontal .checkbox-inline {
  padding-top: 7px;
  margin-top: 0;
  margin-bottom: 0;
}

.scoped-bootstrap .form-horizontal .radio,
.scoped-bootstrap .form-horizontal .checkbox {
  min-height: 27px;
}

.scoped-bootstrap .form-horizontal .form-group {
  margin-right: -15px;
  margin-left: -15px;
}

@media (min-width: 768px) {
  .scoped-bootstrap .form-horizontal .control-label {
    padding-top: 7px;
    margin-bottom: 0;
    text-align: right;
  }
}

.scoped-bootstrap .form-horizontal .has-feedback .form-control-feedback {
  right: 15px;
}

@media (min-width: 768px) {
  .scoped-bootstrap .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 18px;
  }
}

@media (min-width: 768px) {
  .scoped-bootstrap .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}

.scoped-bootstrap .btn {
  display: inline-block;
  padding: 6px 12px;
  margin-bottom: 0;
  font-size: 14px;
  font-weight: normal;
  line-height: 1.42857143;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  -ms-touch-action: manipulation;
  touch-action: manipulation;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 4px;
}

.scoped-bootstrap .btn:focus,
.scoped-bootstrap .btn:active:focus,
.scoped-bootstrap .btn.active:focus,
.scoped-bootstrap .btn.focus,
.scoped-bootstrap .btn:active.focus,
.scoped-bootstrap .btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}

.scoped-bootstrap .btn:hover,
.scoped-bootstrap .btn:focus,
.scoped-bootstrap .btn.focus {
  color: #333;
  text-decoration: none;
}

.scoped-bootstrap .btn:active,
.scoped-bootstrap .btn.active {
  background-image: none;
  outline: 0;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
}

.scoped-bootstrap .btn.disabled,
.scoped-bootstrap .btn[disabled],
.scoped-bootstrap fieldset[disabled] .btn {
  cursor: not-allowed;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
  opacity: .65;
}

.scoped-bootstrap a.btn.disabled,
.scoped-bootstrap fieldset[disabled] a.btn {
  pointer-events: none;
}

.scoped-bootstrap .btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}

.scoped-bootstrap .btn-default:focus,
.scoped-bootstrap .btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}

.scoped-bootstrap .btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}

.scoped-bootstrap .btn-default:active,
.scoped-bootstrap .btn-default.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}

.scoped-bootstrap .btn-default:active:hover,
.scoped-bootstrap .btn-default.active:hover,
.scoped-bootstrap .open > .dropdown-toggle.btn-default:hover,
.scoped-bootstrap .btn-default:active:focus,
.scoped-bootstrap .btn-default.active:focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-default:focus,
.scoped-bootstrap .btn-default:active.focus,
.scoped-bootstrap .btn-default.active.focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}

.scoped-bootstrap .btn-default:active,
.scoped-bootstrap .btn-default.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-default {
  background-image: none;
}

.scoped-bootstrap .btn-default.disabled:hover,
.scoped-bootstrap .btn-default[disabled]:hover,
.scoped-bootstrap fieldset[disabled] .btn-default:hover,
.scoped-bootstrap .btn-default.disabled:focus,
.scoped-bootstrap .btn-default[disabled]:focus,
.scoped-bootstrap fieldset[disabled] .btn-default:focus,
.scoped-bootstrap .btn-default.disabled.focus,
.scoped-bootstrap .btn-default[disabled].focus,
.scoped-bootstrap fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}

.scoped-bootstrap .btn-default .badge {
  color: #fff;
  background-color: #333;
}

.scoped-bootstrap .btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}

.scoped-bootstrap .btn-primary:focus,
.scoped-bootstrap .btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}

.scoped-bootstrap .btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}

.scoped-bootstrap .btn-primary:active,
.scoped-bootstrap .btn-primary.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}

.scoped-bootstrap .btn-primary:active:hover,
.scoped-bootstrap .btn-primary.active:hover,
.scoped-bootstrap .open > .dropdown-toggle.btn-primary:hover,
.scoped-bootstrap .btn-primary:active:focus,
.scoped-bootstrap .btn-primary.active:focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-primary:focus,
.scoped-bootstrap .btn-primary:active.focus,
.scoped-bootstrap .btn-primary.active.focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}

.scoped-bootstrap .btn-primary:active,
.scoped-bootstrap .btn-primary.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-primary {
  background-image: none;
}

.scoped-bootstrap .btn-primary.disabled:hover,
.scoped-bootstrap .btn-primary[disabled]:hover,
.scoped-bootstrap fieldset[disabled] .btn-primary:hover,
.scoped-bootstrap .btn-primary.disabled:focus,
.scoped-bootstrap .btn-primary[disabled]:focus,
.scoped-bootstrap fieldset[disabled] .btn-primary:focus,
.scoped-bootstrap .btn-primary.disabled.focus,
.scoped-bootstrap .btn-primary[disabled].focus,
.scoped-bootstrap fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}

.scoped-bootstrap .btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}

.scoped-bootstrap .btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}

.scoped-bootstrap .btn-success:focus,
.scoped-bootstrap .btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}

.scoped-bootstrap .btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}

.scoped-bootstrap .btn-success:active,
.scoped-bootstrap .btn-success.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}

.scoped-bootstrap .btn-success:active:hover,
.scoped-bootstrap .btn-success.active:hover,
.scoped-bootstrap .open > .dropdown-toggle.btn-success:hover,
.scoped-bootstrap .btn-success:active:focus,
.scoped-bootstrap .btn-success.active:focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-success:focus,
.scoped-bootstrap .btn-success:active.focus,
.scoped-bootstrap .btn-success.active.focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}

.scoped-bootstrap .btn-success:active,
.scoped-bootstrap .btn-success.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-success {
  background-image: none;
}

.scoped-bootstrap .btn-success.disabled:hover,
.scoped-bootstrap .btn-success[disabled]:hover,
.scoped-bootstrap fieldset[disabled] .btn-success:hover,
.scoped-bootstrap .btn-success.disabled:focus,
.scoped-bootstrap .btn-success[disabled]:focus,
.scoped-bootstrap fieldset[disabled] .btn-success:focus,
.scoped-bootstrap .btn-success.disabled.focus,
.scoped-bootstrap .btn-success[disabled].focus,
.scoped-bootstrap fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}

.scoped-bootstrap .btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}

.scoped-bootstrap .btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}

.scoped-bootstrap .btn-info:focus,
.scoped-bootstrap .btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}

.scoped-bootstrap .btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}

.scoped-bootstrap .btn-info:active,
.scoped-bootstrap .btn-info.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}

.scoped-bootstrap .btn-info:active:hover,
.scoped-bootstrap .btn-info.active:hover,
.scoped-bootstrap .open > .dropdown-toggle.btn-info:hover,
.scoped-bootstrap .btn-info:active:focus,
.scoped-bootstrap .btn-info.active:focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-info:focus,
.scoped-bootstrap .btn-info:active.focus,
.scoped-bootstrap .btn-info.active.focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}

.scoped-bootstrap .btn-info:active,
.scoped-bootstrap .btn-info.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-info {
  background-image: none;
}

.scoped-bootstrap .btn-info.disabled:hover,
.scoped-bootstrap .btn-info[disabled]:hover,
.scoped-bootstrap fieldset[disabled] .btn-info:hover,
.scoped-bootstrap .btn-info.disabled:focus,
.scoped-bootstrap .btn-info[disabled]:focus,
.scoped-bootstrap fieldset[disabled] .btn-info:focus,
.scoped-bootstrap .btn-info.disabled.focus,
.scoped-bootstrap .btn-info[disabled].focus,
.scoped-bootstrap fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}

.scoped-bootstrap .btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}

.scoped-bootstrap .btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}

.scoped-bootstrap .btn-warning:focus,
.scoped-bootstrap .btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}

.scoped-bootstrap .btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}

.scoped-bootstrap .btn-warning:active,
.scoped-bootstrap .btn-warning.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}

.scoped-bootstrap .btn-warning:active:hover,
.scoped-bootstrap .btn-warning.active:hover,
.scoped-bootstrap .open > .dropdown-toggle.btn-warning:hover,
.scoped-bootstrap .btn-warning:active:focus,
.scoped-bootstrap .btn-warning.active:focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-warning:focus,
.scoped-bootstrap .btn-warning:active.focus,
.scoped-bootstrap .btn-warning.active.focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}

.scoped-bootstrap .btn-warning:active,
.scoped-bootstrap .btn-warning.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-warning {
  background-image: none;
}

.scoped-bootstrap .btn-warning.disabled:hover,
.scoped-bootstrap .btn-warning[disabled]:hover,
.scoped-bootstrap fieldset[disabled] .btn-warning:hover,
.scoped-bootstrap .btn-warning.disabled:focus,
.scoped-bootstrap .btn-warning[disabled]:focus,
.scoped-bootstrap fieldset[disabled] .btn-warning:focus,
.scoped-bootstrap .btn-warning.disabled.focus,
.scoped-bootstrap .btn-warning[disabled].focus,
.scoped-bootstrap fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}

.scoped-bootstrap .btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}

.scoped-bootstrap .btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}

.scoped-bootstrap .btn-danger:focus,
.scoped-bootstrap .btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}

.scoped-bootstrap .btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}

.scoped-bootstrap .btn-danger:active,
.scoped-bootstrap .btn-danger.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}

.scoped-bootstrap .btn-danger:active:hover,
.scoped-bootstrap .btn-danger.active:hover,
.scoped-bootstrap .open > .dropdown-toggle.btn-danger:hover,
.scoped-bootstrap .btn-danger:active:focus,
.scoped-bootstrap .btn-danger.active:focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-danger:focus,
.scoped-bootstrap .btn-danger:active.focus,
.scoped-bootstrap .btn-danger.active.focus,
.scoped-bootstrap .open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}

.scoped-bootstrap .btn-danger:active,
.scoped-bootstrap .btn-danger.active,
.scoped-bootstrap .open > .dropdown-toggle.btn-danger {
  background-image: none;
}

.scoped-bootstrap .btn-danger.disabled:hover,
.scoped-bootstrap .btn-danger[disabled]:hover,
.scoped-bootstrap fieldset[disabled] .btn-danger:hover,
.scoped-bootstrap .btn-danger.disabled:focus,
.scoped-bootstrap .btn-danger[disabled]:focus,
.scoped-bootstrap fieldset[disabled] .btn-danger:focus,
.scoped-bootstrap .btn-danger.disabled.focus,
.scoped-bootstrap .btn-danger[disabled].focus,
.scoped-bootstrap fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}

.scoped-bootstrap .btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}

.scoped-bootstrap .btn-link {
  font-weight: normal;
  color: #337ab7;
  border-radius: 0;
}

.scoped-bootstrap .btn-link,
.scoped-bootstrap .btn-link:active,
.scoped-bootstrap .btn-link.active,
.scoped-bootstrap .btn-link[disabled],
.scoped-bootstrap fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}

.scoped-bootstrap .btn-link,
.scoped-bootstrap .btn-link:hover,
.scoped-bootstrap .btn-link:focus,
.scoped-bootstrap .btn-link:active {
  border-color: transparent;
}

.scoped-bootstrap .btn-link:hover,
.scoped-bootstrap .btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}

.scoped-bootstrap .btn-link[disabled]:hover,
.scoped-bootstrap fieldset[disabled] .btn-link:hover,
.scoped-bootstrap .btn-link[disabled]:focus,
.scoped-bootstrap fieldset[disabled] .btn-link:focus {
  color: #777;
  text-decoration: none;
}

.scoped-bootstrap .btn-lg,
.scoped-bootstrap .btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 18px;
  line-height: 1.3333333;
  border-radius: 6px;
}

.scoped-bootstrap .btn-sm,
.scoped-bootstrap .btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 3px;
}

.scoped-bootstrap .btn-xs,
.scoped-bootstrap .btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 3px;
}

.scoped-bootstrap .btn-block {
  display: block;
  width: 100%;
}

.scoped-bootstrap .btn-block + .btn-block {
  margin-top: 5px;
}

.scoped-bootstrap input[type="submit"].btn-block,
.scoped-bootstrap input[type="reset"].btn-block,
.scoped-bootstrap input[type="button"].btn-block {
  width: 100%;
}

.scoped-bootstrap .fade {
  opacity: 0;
  -webkit-transition: opacity .15s linear;
  -o-transition: opacity .15s linear;
  transition: opacity .15s linear;
}

.scoped-bootstrap .fade.in {
  opacity: 1;
}

.scoped-bootstrap .collapse {
  display: none;
}

.scoped-bootstrap .collapse.in {
  display: block;
}

.scoped-bootstrap tr.collapse.in {
  display: table-row;
}

.scoped-bootstrap tbody.collapse.in {
  display: table-row-group;
}

.scoped-bootstrap .collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-timing-function: ease;
  -o-transition-timing-function: ease;
  transition-timing-function: ease;
  -webkit-transition-duration: .35s;
  -o-transition-duration: .35s;
  transition-duration: .35s;
  -webkit-transition-property: height, visibility;
  -o-transition-property: height, visibility;
  transition-property: height, visibility;
}

.scoped-bootstrap .caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}

.scoped-bootstrap .dropup,
.scoped-bootstrap .dropdown {
  position: relative;
}

.scoped-bootstrap .dropdown-toggle:focus {
  outline: 0;
}

.scoped-bootstrap .dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  font-size: 14px;
  text-align: left;
  list-style: none;
  background-color: #fff;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, .15);
  border-radius: 4px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, .175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, .175);
}

.scoped-bootstrap .dropdown-menu.pull-right {
  right: 0;
  left: auto;
}

.scoped-bootstrap .dropdown-menu .divider {
  height: 1px;
  margin: 9px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}

.scoped-bootstrap .dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333;
  white-space: nowrap;
}

.scoped-bootstrap .dropdown-menu > li > a:hover,
.scoped-bootstrap .dropdown-menu > li > a:focus {
  color: #262626;
  text-decoration: none;
  background-color: #f5f5f5;
}

.scoped-bootstrap .dropdown-menu > .active > a,
.scoped-bootstrap .dropdown-menu > .active > a:hover,
.scoped-bootstrap .dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  background-color: #337ab7;
  outline: 0;
}

.scoped-bootstrap .dropdown-menu > .disabled > a,
.scoped-bootstrap .dropdown-menu > .disabled > a:hover,
.scoped-bootstrap .dropdown-menu > .disabled > a:focus {
  color: #777;
}

.scoped-bootstrap .dropdown-menu > .disabled > a:hover,
.scoped-bootstrap .dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  cursor: not-allowed;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
}

.scoped-bootstrap .open > .dropdown-menu {
  display: block;
}

.scoped-bootstrap .open > a {
  outline: 0;
}

.scoped-bootstrap .dropdown-menu-right {
  right: 0;
  left: auto;
}

.scoped-bootstrap .dropdown-menu-left {
  right: auto;
  left: 0;
}

.scoped-bootstrap .dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777;
  white-space: nowrap;
}

.scoped-bootstrap .dropdown-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 990;
}

.scoped-bootstrap .pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}

.scoped-bootstrap .dropup .caret,
.scoped-bootstrap .navbar-fixed-bottom .dropdown .caret {
  content: "";
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
}

.scoped-bootstrap .dropup .dropdown-menu,
.scoped-bootstrap .navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-right .dropdown-menu {
    right: 0;
    left: auto;
  }

  .scoped-bootstrap .navbar-right .dropdown-menu-left {
    right: auto;
    left: 0;
  }
}

.scoped-bootstrap .btn-group,
.scoped-bootstrap .btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}

.scoped-bootstrap .btn-group > .btn,
.scoped-bootstrap .btn-group-vertical > .btn {
  position: relative;
  float: left;
}

.scoped-bootstrap .btn-group > .btn:hover,
.scoped-bootstrap .btn-group-vertical > .btn:hover,
.scoped-bootstrap .btn-group > .btn:focus,
.scoped-bootstrap .btn-group-vertical > .btn:focus,
.scoped-bootstrap .btn-group > .btn:active,
.scoped-bootstrap .btn-group-vertical > .btn:active,
.scoped-bootstrap .btn-group > .btn.active,
.scoped-bootstrap .btn-group-vertical > .btn.active {
  z-index: 2;
}

.scoped-bootstrap .btn-group .btn + .btn,
.scoped-bootstrap .btn-group .btn + .btn-group,
.scoped-bootstrap .btn-group .btn-group + .btn,
.scoped-bootstrap .btn-group .btn-group + .btn-group {
  margin-left: -1px;
}

.scoped-bootstrap .btn-toolbar {
  margin-left: -5px;
}

.scoped-bootstrap .btn-toolbar .btn,
.scoped-bootstrap .btn-toolbar .btn-group,
.scoped-bootstrap .btn-toolbar .input-group {
  float: left;
}

.scoped-bootstrap .btn-toolbar > .btn,
.scoped-bootstrap .btn-toolbar > .btn-group,
.scoped-bootstrap .btn-toolbar > .input-group {
  margin-left: 5px;
}

.scoped-bootstrap .btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}

.scoped-bootstrap .btn-group > .btn:first-child {
  margin-left: 0;
}

.scoped-bootstrap .btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.scoped-bootstrap .btn-group > .btn:last-child:not(:first-child),
.scoped-bootstrap .btn-group > .dropdown-toggle:not(:first-child) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.scoped-bootstrap .btn-group > .btn-group {
  float: left;
}

.scoped-bootstrap .btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}

.scoped-bootstrap .btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.scoped-bootstrap .btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.scoped-bootstrap .btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.scoped-bootstrap .btn-group .dropdown-toggle:active,
.scoped-bootstrap .btn-group.open .dropdown-toggle {
  outline: 0;
}

.scoped-bootstrap .btn-group > .btn + .dropdown-toggle {
  padding-right: 8px;
  padding-left: 8px;
}

.scoped-bootstrap .btn-group > .btn-lg + .dropdown-toggle {
  padding-right: 12px;
  padding-left: 12px;
}

.scoped-bootstrap .btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
}

.scoped-bootstrap .btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}

.scoped-bootstrap .btn .caret {
  margin-left: 0;
}

.scoped-bootstrap .btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}

.scoped-bootstrap .dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}

.scoped-bootstrap .btn-group-vertical > .btn,
.scoped-bootstrap .btn-group-vertical > .btn-group,
.scoped-bootstrap .btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}

.scoped-bootstrap .btn-group-vertical > .btn-group > .btn {
  float: none;
}

.scoped-bootstrap .btn-group-vertical > .btn + .btn,
.scoped-bootstrap .btn-group-vertical > .btn + .btn-group,
.scoped-bootstrap .btn-group-vertical > .btn-group + .btn,
.scoped-bootstrap .btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}

.scoped-bootstrap .btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}

.scoped-bootstrap .btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.scoped-bootstrap .btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-left-radius: 0;
  border-top-right-radius: 0;
  border-bottom-right-radius: 4px;
  border-bottom-left-radius: 4px;
}

.scoped-bootstrap .btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}

.scoped-bootstrap .btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.scoped-bootstrap .btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.scoped-bootstrap .btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.scoped-bootstrap .btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}

.scoped-bootstrap .btn-group-justified > .btn,
.scoped-bootstrap .btn-group-justified > .btn-group {
  display: table-cell;
  float: none;
  width: 1%;
}

.scoped-bootstrap .btn-group-justified > .btn-group .btn {
  width: 100%;
}

.scoped-bootstrap .btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}

.scoped-bootstrap [data-toggle="buttons"] > .btn input[type="radio"],
.scoped-bootstrap [data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
.scoped-bootstrap [data-toggle="buttons"] > .btn input[type="checkbox"],
.scoped-bootstrap [data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}

.scoped-bootstrap .input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}

.scoped-bootstrap .input-group[class*="col-"] {
  float: none;
  padding-right: 0;
  padding-left: 0;
}

.scoped-bootstrap .input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}

.scoped-bootstrap .input-group .form-control:focus {
  z-index: 3;
}

.scoped-bootstrap .input-group-lg > .form-control,
.scoped-bootstrap .input-group-lg > .input-group-addon,
.scoped-bootstrap .input-group-lg > .input-group-btn > .btn {
  height: 46px;
  padding: 10px 16px;
  font-size: 18px;
  line-height: 1.3333333;
  border-radius: 6px;
}

.scoped-bootstrap select.input-group-lg > .form-control,
.scoped-bootstrap select.input-group-lg > .input-group-addon,
.scoped-bootstrap select.input-group-lg > .input-group-btn > .btn {
  height: 46px;
  line-height: 46px;
}

.scoped-bootstrap textarea.input-group-lg > .form-control,
.scoped-bootstrap textarea.input-group-lg > .input-group-addon,
.scoped-bootstrap textarea.input-group-lg > .input-group-btn > .btn,
.scoped-bootstrap select[multiple].input-group-lg > .form-control,
.scoped-bootstrap select[multiple].input-group-lg > .input-group-addon,
.scoped-bootstrap select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}

.scoped-bootstrap .input-group-sm > .form-control,
.scoped-bootstrap .input-group-sm > .input-group-addon,
.scoped-bootstrap .input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 3px;
}

.scoped-bootstrap select.input-group-sm > .form-control,
.scoped-bootstrap select.input-group-sm > .input-group-addon,
.scoped-bootstrap select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}

.scoped-bootstrap textarea.input-group-sm > .form-control,
.scoped-bootstrap textarea.input-group-sm > .input-group-addon,
.scoped-bootstrap textarea.input-group-sm > .input-group-btn > .btn,
.scoped-bootstrap select[multiple].input-group-sm > .form-control,
.scoped-bootstrap select[multiple].input-group-sm > .input-group-addon,
.scoped-bootstrap select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}

.scoped-bootstrap .input-group-addon,
.scoped-bootstrap .input-group-btn,
.scoped-bootstrap .input-group .form-control {
  display: table-cell;
}

.scoped-bootstrap .input-group-addon:not(:first-child):not(:last-child),
.scoped-bootstrap .input-group-btn:not(:first-child):not(:last-child),
.scoped-bootstrap .input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}

.scoped-bootstrap .input-group-addon,
.scoped-bootstrap .input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}

.scoped-bootstrap .input-group-addon {
  padding: 6px 12px;
  font-size: 14px;
  font-weight: normal;
  line-height: 1;
  color: #555;
  text-align: center;
  background-color: #eee;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.scoped-bootstrap .input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 3px;
}

.scoped-bootstrap .input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 18px;
  border-radius: 6px;
}

.scoped-bootstrap .input-group-addon input[type="radio"],
.scoped-bootstrap .input-group-addon input[type="checkbox"] {
  margin-top: 0;
}

.scoped-bootstrap .input-group .form-control:first-child,
.scoped-bootstrap .input-group-addon:first-child,
.scoped-bootstrap .input-group-btn:first-child > .btn,
.scoped-bootstrap .input-group-btn:first-child > .btn-group > .btn,
.scoped-bootstrap .input-group-btn:first-child > .dropdown-toggle,
.scoped-bootstrap .input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.scoped-bootstrap .input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.scoped-bootstrap .input-group-addon:first-child {
  border-right: 0;
}

.scoped-bootstrap .input-group .form-control:last-child,
.scoped-bootstrap .input-group-addon:last-child,
.scoped-bootstrap .input-group-btn:last-child > .btn,
.scoped-bootstrap .input-group-btn:last-child > .btn-group > .btn,
.scoped-bootstrap .input-group-btn:last-child > .dropdown-toggle,
.scoped-bootstrap .input-group-btn:first-child > .btn:not(:first-child),
.scoped-bootstrap .input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.scoped-bootstrap .input-group-addon:last-child {
  border-left: 0;
}

.scoped-bootstrap .input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}

.scoped-bootstrap .input-group-btn > .btn {
  position: relative;
}

.scoped-bootstrap .input-group-btn > .btn + .btn {
  margin-left: -1px;
}

.scoped-bootstrap .input-group-btn > .btn:hover,
.scoped-bootstrap .input-group-btn > .btn:focus,
.scoped-bootstrap .input-group-btn > .btn:active {
  z-index: 2;
}

.scoped-bootstrap .input-group-btn:first-child > .btn,
.scoped-bootstrap .input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}

.scoped-bootstrap .input-group-btn:last-child > .btn,
.scoped-bootstrap .input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}

.scoped-bootstrap .nav {
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}

.scoped-bootstrap .nav > li {
  position: relative;
  display: block;
}

.scoped-bootstrap .nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}

.scoped-bootstrap .nav > li > a:hover,
.scoped-bootstrap .nav > li > a:focus {
  text-decoration: none;
  background-color: #eee;
}

.scoped-bootstrap .nav > li.disabled > a {
  color: #777;
}

.scoped-bootstrap .nav > li.disabled > a:hover,
.scoped-bootstrap .nav > li.disabled > a:focus {
  color: #777;
  text-decoration: none;
  cursor: not-allowed;
  background-color: transparent;
}

.scoped-bootstrap .nav .open > a,
.scoped-bootstrap .nav .open > a:hover,
.scoped-bootstrap .nav .open > a:focus {
  background-color: #eee;
  border-color: #337ab7;
}

.scoped-bootstrap .nav .nav-divider {
  height: 1px;
  margin: 9px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}

.scoped-bootstrap .nav > li > a > img {
  max-width: none;
}

.scoped-bootstrap .nav-tabs {
  border-bottom: 1px solid #ddd;
}

.scoped-bootstrap .nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}

.scoped-bootstrap .nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 4px 4px 0 0;
}

.scoped-bootstrap .nav-tabs > li > a:hover {
  border-color: #eee #eee #ddd;
}

.scoped-bootstrap .nav-tabs > li.active > a,
.scoped-bootstrap .nav-tabs > li.active > a:hover,
.scoped-bootstrap .nav-tabs > li.active > a:focus {
  color: #555;
  cursor: default;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
}

.scoped-bootstrap .nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}

.scoped-bootstrap .nav-tabs.nav-justified > li {
  float: none;
}

.scoped-bootstrap .nav-tabs.nav-justified > li > a {
  margin-bottom: 5px;
  text-align: center;
}

.scoped-bootstrap .nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}

@media (min-width: 768px) {
  .scoped-bootstrap .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }

  .scoped-bootstrap .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}

.scoped-bootstrap .nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 4px;
}

.scoped-bootstrap .nav-tabs.nav-justified > .active > a,
.scoped-bootstrap .nav-tabs.nav-justified > .active > a:hover,
.scoped-bootstrap .nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}

@media (min-width: 768px) {
  .scoped-bootstrap .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 4px 4px 0 0;
  }

  .scoped-bootstrap .nav-tabs.nav-justified > .active > a,
  .scoped-bootstrap .nav-tabs.nav-justified > .active > a:hover,
  .scoped-bootstrap .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}

.scoped-bootstrap .nav-pills > li {
  float: left;
}

.scoped-bootstrap .nav-pills > li > a {
  border-radius: 4px;
}

.scoped-bootstrap .nav-pills > li + li {
  margin-left: 2px;
}

.scoped-bootstrap .nav-pills > li.active > a,
.scoped-bootstrap .nav-pills > li.active > a:hover,
.scoped-bootstrap .nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}

.scoped-bootstrap .nav-stacked > li {
  float: none;
}

.scoped-bootstrap .nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}

.scoped-bootstrap .nav-justified {
  width: 100%;
}

.scoped-bootstrap .nav-justified > li {
  float: none;
}

.scoped-bootstrap .nav-justified > li > a {
  margin-bottom: 5px;
  text-align: center;
}

.scoped-bootstrap .nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}

@media (min-width: 768px) {
  .scoped-bootstrap .nav-justified > li {
    display: table-cell;
    width: 1%;
  }

  .scoped-bootstrap .nav-justified > li > a {
    margin-bottom: 0;
  }
}

.scoped-bootstrap .nav-tabs-justified {
  border-bottom: 0;
}

.scoped-bootstrap .nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 4px;
}

.scoped-bootstrap .nav-tabs-justified > .active > a,
.scoped-bootstrap .nav-tabs-justified > .active > a:hover,
.scoped-bootstrap .nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}

@media (min-width: 768px) {
  .scoped-bootstrap .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 4px 4px 0 0;
  }

  .scoped-bootstrap .nav-tabs-justified > .active > a,
  .scoped-bootstrap .nav-tabs-justified > .active > a:hover,
  .scoped-bootstrap .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}

.scoped-bootstrap .tab-content > .tab-pane {
  display: none;
}

.scoped-bootstrap .tab-content > .active {
  display: block;
}

.scoped-bootstrap .nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.scoped-bootstrap .navbar {
  position: relative;
  min-height: 50px;
  margin-bottom: 20px;
  border: 1px solid transparent;
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar {
    border-radius: 4px;
  }
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-header {
    float: left;
  }
}

.scoped-bootstrap .navbar-collapse {
  padding-right: 15px;
  padding-left: 15px;
  overflow-x: visible;
  -webkit-overflow-scrolling: touch;
  border-top: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, .1);
}

.scoped-bootstrap .navbar-collapse.in {
  overflow-y: auto;
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-collapse {
    width: auto;
    border-top: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }

  .scoped-bootstrap .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }

  .scoped-bootstrap .navbar-collapse.in {
    overflow-y: visible;
  }

  .scoped-bootstrap .navbar-fixed-top .navbar-collapse,
  .scoped-bootstrap .navbar-static-top .navbar-collapse,
  .scoped-bootstrap .navbar-fixed-bottom .navbar-collapse {
    padding-right: 0;
    padding-left: 0;
  }
}

.scoped-bootstrap .navbar-fixed-top .navbar-collapse,
.scoped-bootstrap .navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}

@media (max-device-width: 480px) and (orientation: landscape) {
  .scoped-bootstrap .navbar-fixed-top .navbar-collapse,
  .scoped-bootstrap .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}

.scoped-bootstrap .container > .navbar-header,
.scoped-bootstrap .container-fluid > .navbar-header,
.scoped-bootstrap .container > .navbar-collapse,
.scoped-bootstrap .container-fluid > .navbar-collapse {
  margin-right: -15px;
  margin-left: -15px;
}

@media (min-width: 768px) {
  .scoped-bootstrap .container > .navbar-header,
  .scoped-bootstrap .container-fluid > .navbar-header,
  .scoped-bootstrap .container > .navbar-collapse,
  .scoped-bootstrap .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}

.scoped-bootstrap .navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-static-top {
    border-radius: 0;
  }
}

.scoped-bootstrap .navbar-fixed-top,
.scoped-bootstrap .navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-fixed-top,
  .scoped-bootstrap .navbar-fixed-bottom {
    border-radius: 0;
  }
}

.scoped-bootstrap .navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}

.scoped-bootstrap .navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}

.scoped-bootstrap .navbar-brand {
  float: left;
  height: 50px;
  padding: 15px 15px;
  font-size: 18px;
  line-height: 20px;
}

.scoped-bootstrap .navbar-brand:hover,
.scoped-bootstrap .navbar-brand:focus {
  text-decoration: none;
}

.scoped-bootstrap .navbar-brand > img {
  display: block;
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar > .container .navbar-brand,
  .scoped-bootstrap .navbar > .container-fluid .navbar-brand {
    margin-left: -15px;
  }
}

.scoped-bootstrap .navbar-toggle {
  position: relative;
  float: right;
  padding: 9px 10px;
  margin-top: 8px;
  margin-right: 15px;
  margin-bottom: 8px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 4px;
}

.scoped-bootstrap .navbar-toggle:focus {
  outline: 0;
}

.scoped-bootstrap .navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}

.scoped-bootstrap .navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-toggle {
    display: none;
  }
}

.scoped-bootstrap .navbar-nav {
  margin: 7.5px -15px;
}

.scoped-bootstrap .navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 20px;
}

@media (max-width: 767px) {
  .scoped-bootstrap .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }

  .scoped-bootstrap .navbar-nav .open .dropdown-menu > li > a,
  .scoped-bootstrap .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }

  .scoped-bootstrap .navbar-nav .open .dropdown-menu > li > a {
    line-height: 20px;
  }

  .scoped-bootstrap .navbar-nav .open .dropdown-menu > li > a:hover,
  .scoped-bootstrap .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-nav {
    float: left;
    margin: 0;
  }

  .scoped-bootstrap .navbar-nav > li {
    float: left;
  }

  .scoped-bootstrap .navbar-nav > li > a {
    padding-top: 15px;
    padding-bottom: 15px;
  }
}

.scoped-bootstrap .navbar-form {
  padding: 10px 15px;
  margin-top: 8px;
  margin-right: -15px;
  margin-bottom: 8px;
  margin-left: -15px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .1), 0 1px 0 rgba(255, 255, 255, .1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, .1), 0 1px 0 rgba(255, 255, 255, .1);
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }

  .scoped-bootstrap .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }

  .scoped-bootstrap .navbar-form .form-control-static {
    display: inline-block;
  }

  .scoped-bootstrap .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }

  .scoped-bootstrap .navbar-form .input-group .input-group-addon,
  .scoped-bootstrap .navbar-form .input-group .input-group-btn,
  .scoped-bootstrap .navbar-form .input-group .form-control {
    width: auto;
  }

  .scoped-bootstrap .navbar-form .input-group > .form-control {
    width: 100%;
  }

  .scoped-bootstrap .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }

  .scoped-bootstrap .navbar-form .radio,
  .scoped-bootstrap .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }

  .scoped-bootstrap .navbar-form .radio label,
  .scoped-bootstrap .navbar-form .checkbox label {
    padding-left: 0;
  }

  .scoped-bootstrap .navbar-form .radio input[type="radio"],
  .scoped-bootstrap .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }

  .scoped-bootstrap .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}

@media (max-width: 767px) {
  .scoped-bootstrap .navbar-form .form-group {
    margin-bottom: 5px;
  }

  .scoped-bootstrap .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-form {
    width: auto;
    padding-top: 0;
    padding-bottom: 0;
    margin-right: 0;
    margin-left: 0;
    border: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}

.scoped-bootstrap .navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.scoped-bootstrap .navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.scoped-bootstrap .navbar-btn {
  margin-top: 8px;
  margin-bottom: 8px;
}

.scoped-bootstrap .navbar-btn.btn-sm {
  margin-top: 10px;
  margin-bottom: 10px;
}

.scoped-bootstrap .navbar-btn.btn-xs {
  margin-top: 14px;
  margin-bottom: 14px;
}

.scoped-bootstrap .navbar-text {
  margin-top: 15px;
  margin-bottom: 15px;
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-text {
    float: left;
    margin-right: 15px;
    margin-left: 15px;
  }
}

@media (min-width: 768px) {
  .scoped-bootstrap .navbar-left {
    float: left !important;
  }

  .scoped-bootstrap .navbar-right {
    float: right !important;
    margin-right: -15px;
  }

  .scoped-bootstrap .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}

.scoped-bootstrap .navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}

.scoped-bootstrap .navbar-default .navbar-brand {
  color: #777;
}

.scoped-bootstrap .navbar-default .navbar-brand:hover,
.scoped-bootstrap .navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}

.scoped-bootstrap .navbar-default .navbar-text {
  color: #777;
}

.scoped-bootstrap .navbar-default .navbar-nav > li > a {
  color: #777;
}

.scoped-bootstrap .navbar-default .navbar-nav > li > a:hover,
.scoped-bootstrap .navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}

.scoped-bootstrap .navbar-default .navbar-nav > .active > a,
.scoped-bootstrap .navbar-default .navbar-nav > .active > a:hover,
.scoped-bootstrap .navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}

.scoped-bootstrap .navbar-default .navbar-nav > .disabled > a,
.scoped-bootstrap .navbar-default .navbar-nav > .disabled > a:hover,
.scoped-bootstrap .navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}

.scoped-bootstrap .navbar-default .navbar-toggle {
  border-color: #ddd;
}

.scoped-bootstrap .navbar-default .navbar-toggle:hover,
.scoped-bootstrap .navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}

.scoped-bootstrap .navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}

.scoped-bootstrap .navbar-default .navbar-collapse,
.scoped-bootstrap .navbar-default .navbar-form {
  border-color: #e7e7e7;
}

.scoped-bootstrap .navbar-default .navbar-nav > .open > a,
.scoped-bootstrap .navbar-default .navbar-nav > .open > a:hover,
.scoped-bootstrap .navbar-default .navbar-nav > .open > a:focus {
  color: #555;
  background-color: #e7e7e7;
}

@media (max-width: 767px) {
  .scoped-bootstrap .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }

  .scoped-bootstrap .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .scoped-bootstrap .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }

  .scoped-bootstrap .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .scoped-bootstrap .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .scoped-bootstrap .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }

  .scoped-bootstrap .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .scoped-bootstrap .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .scoped-bootstrap .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}

.scoped-bootstrap .navbar-default .navbar-link {
  color: #777;
}

.scoped-bootstrap .navbar-default .navbar-link:hover {
  color: #333;
}

.scoped-bootstrap .navbar-default .btn-link {
  color: #777;
}

.scoped-bootstrap .navbar-default .btn-link:hover,
.scoped-bootstrap .navbar-default .btn-link:focus {
  color: #333;
}

.scoped-bootstrap .navbar-default .btn-link[disabled]:hover,
.scoped-bootstrap fieldset[disabled] .navbar-default .btn-link:hover,
.scoped-bootstrap .navbar-default .btn-link[disabled]:focus,
.scoped-bootstrap fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}

.scoped-bootstrap .navbar-inverse {
  background-color: #222;
  border-color: #080808;
}

.scoped-bootstrap .navbar-inverse .navbar-brand {
  color: #9d9d9d;
}

.scoped-bootstrap .navbar-inverse .navbar-brand:hover,
.scoped-bootstrap .navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}

.scoped-bootstrap .navbar-inverse .navbar-text {
  color: #9d9d9d;
}

.scoped-bootstrap .navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}

.scoped-bootstrap .navbar-inverse .navbar-nav > li > a:hover,
.scoped-bootstrap .navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}

.scoped-bootstrap .navbar-inverse .navbar-nav > .active > a,
.scoped-bootstrap .navbar-inverse .navbar-nav > .active > a:hover,
.scoped-bootstrap .navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}

.scoped-bootstrap .navbar-inverse .navbar-nav > .disabled > a,
.scoped-bootstrap .navbar-inverse .navbar-nav > .disabled > a:hover,
.scoped-bootstrap .navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}

.scoped-bootstrap .navbar-inverse .navbar-toggle {
  border-color: #333;
}

.scoped-bootstrap .navbar-inverse .navbar-toggle:hover,
.scoped-bootstrap .navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}

.scoped-bootstrap .navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}

.scoped-bootstrap .navbar-inverse .navbar-collapse,
.scoped-bootstrap .navbar-inverse .navbar-form {
  border-color: #101010;
}

.scoped-bootstrap .navbar-inverse .navbar-nav > .open > a,
.scoped-bootstrap .navbar-inverse .navbar-nav > .open > a:hover,
.scoped-bootstrap .navbar-inverse .navbar-nav > .open > a:focus {
  color: #fff;
  background-color: #080808;
}

@media (max-width: 767px) {
  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }

  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }

  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }

  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }

  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }

  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .scoped-bootstrap .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}

.scoped-bootstrap .navbar-inverse .navbar-link {
  color: #9d9d9d;
}

.scoped-bootstrap .navbar-inverse .navbar-link:hover {
  color: #fff;
}

.scoped-bootstrap .navbar-inverse .btn-link {
  color: #9d9d9d;
}

.scoped-bootstrap .navbar-inverse .btn-link:hover,
.scoped-bootstrap .navbar-inverse .btn-link:focus {
  color: #fff;
}

.scoped-bootstrap .navbar-inverse .btn-link[disabled]:hover,
.scoped-bootstrap fieldset[disabled] .navbar-inverse .btn-link:hover,
.scoped-bootstrap .navbar-inverse .btn-link[disabled]:focus,
.scoped-bootstrap fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}

.scoped-bootstrap .breadcrumb {
  padding: 8px 15px;
  margin-bottom: 20px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 4px;
}

.scoped-bootstrap .breadcrumb > li {
  display: inline-block;
}

.scoped-bootstrap .breadcrumb > li + li:before {
  padding: 0 5px;
  color: #ccc;
  content: "/\A0";
}

.scoped-bootstrap .breadcrumb > .active {
  color: #777;
}

.scoped-bootstrap .pagination {
  display: inline-block;
  padding-left: 0;
  margin: 20px 0;
  border-radius: 4px;
}

.scoped-bootstrap .pagination > li {
  display: inline;
}

.scoped-bootstrap .pagination > li > a,
.scoped-bootstrap .pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  margin-left: -1px;
  line-height: 1.42857143;
  color: #337ab7;
  text-decoration: none;
  background-color: #fff;
  border: 1px solid #ddd;
}

.scoped-bootstrap .pagination > li:first-child > a,
.scoped-bootstrap .pagination > li:first-child > span {
  margin-left: 0;
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}

.scoped-bootstrap .pagination > li:last-child > a,
.scoped-bootstrap .pagination > li:last-child > span {
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}

.scoped-bootstrap .pagination > li > a:hover,
.scoped-bootstrap .pagination > li > span:hover,
.scoped-bootstrap .pagination > li > a:focus,
.scoped-bootstrap .pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eee;
  border-color: #ddd;
}

.scoped-bootstrap .pagination > .active > a,
.scoped-bootstrap .pagination > .active > span,
.scoped-bootstrap .pagination > .active > a:hover,
.scoped-bootstrap .pagination > .active > span:hover,
.scoped-bootstrap .pagination > .active > a:focus,
.scoped-bootstrap .pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  cursor: default;
  background-color: #337ab7;
  border-color: #337ab7;
}

.scoped-bootstrap .pagination > .disabled > span,
.scoped-bootstrap .pagination > .disabled > span:hover,
.scoped-bootstrap .pagination > .disabled > span:focus,
.scoped-bootstrap .pagination > .disabled > a,
.scoped-bootstrap .pagination > .disabled > a:hover,
.scoped-bootstrap .pagination > .disabled > a:focus {
  color: #777;
  cursor: not-allowed;
  background-color: #fff;
  border-color: #ddd;
}

.scoped-bootstrap .pagination-lg > li > a,
.scoped-bootstrap .pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 18px;
  line-height: 1.3333333;
}

.scoped-bootstrap .pagination-lg > li:first-child > a,
.scoped-bootstrap .pagination-lg > li:first-child > span {
  border-top-left-radius: 6px;
  border-bottom-left-radius: 6px;
}

.scoped-bootstrap .pagination-lg > li:last-child > a,
.scoped-bootstrap .pagination-lg > li:last-child > span {
  border-top-right-radius: 6px;
  border-bottom-right-radius: 6px;
}

.scoped-bootstrap .pagination-sm > li > a,
.scoped-bootstrap .pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}

.scoped-bootstrap .pagination-sm > li:first-child > a,
.scoped-bootstrap .pagination-sm > li:first-child > span {
  border-top-left-radius: 3px;
  border-bottom-left-radius: 3px;
}

.scoped-bootstrap .pagination-sm > li:last-child > a,
.scoped-bootstrap .pagination-sm > li:last-child > span {
  border-top-right-radius: 3px;
  border-bottom-right-radius: 3px;
}

.scoped-bootstrap .pager {
  padding-left: 0;
  margin: 20px 0;
  text-align: center;
  list-style: none;
}

.scoped-bootstrap .pager li {
  display: inline;
}

.scoped-bootstrap .pager li > a,
.scoped-bootstrap .pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}

.scoped-bootstrap .pager li > a:hover,
.scoped-bootstrap .pager li > a:focus {
  text-decoration: none;
  background-color: #eee;
}

.scoped-bootstrap .pager .next > a,
.scoped-bootstrap .pager .next > span {
  float: right;
}

.scoped-bootstrap .pager .previous > a,
.scoped-bootstrap .pager .previous > span {
  float: left;
}

.scoped-bootstrap .pager .disabled > a,
.scoped-bootstrap .pager .disabled > a:hover,
.scoped-bootstrap .pager .disabled > a:focus,
.scoped-bootstrap .pager .disabled > span {
  color: #777;
  cursor: not-allowed;
  background-color: #fff;
}

.scoped-bootstrap .label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}

.scoped-bootstrap a.label:hover,
.scoped-bootstrap a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}

.scoped-bootstrap .label:empty {
  display: none;
}

.scoped-bootstrap .btn .label {
  position: relative;
  top: -1px;
}

.scoped-bootstrap .label-default {
  background-color: #777;
}

.scoped-bootstrap .label-default[href]:hover,
.scoped-bootstrap .label-default[href]:focus {
  background-color: #5e5e5e;
}

.scoped-bootstrap .label-primary {
  background-color: #337ab7;
}

.scoped-bootstrap .label-primary[href]:hover,
.scoped-bootstrap .label-primary[href]:focus {
  background-color: #286090;
}

.scoped-bootstrap .label-success {
  background-color: #5cb85c;
}

.scoped-bootstrap .label-success[href]:hover,
.scoped-bootstrap .label-success[href]:focus {
  background-color: #449d44;
}

.scoped-bootstrap .label-info {
  background-color: #5bc0de;
}

.scoped-bootstrap .label-info[href]:hover,
.scoped-bootstrap .label-info[href]:focus {
  background-color: #31b0d5;
}

.scoped-bootstrap .label-warning {
  background-color: #f0ad4e;
}

.scoped-bootstrap .label-warning[href]:hover,
.scoped-bootstrap .label-warning[href]:focus {
  background-color: #ec971f;
}

.scoped-bootstrap .label-danger {
  background-color: #d9534f;
}

.scoped-bootstrap .label-danger[href]:hover,
.scoped-bootstrap .label-danger[href]:focus {
  background-color: #c9302c;
}

.scoped-bootstrap .badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  background-color: #777;
  border-radius: 10px;
}

.scoped-bootstrap .badge:empty {
  display: none;
}

.scoped-bootstrap .btn .badge {
  position: relative;
  top: -1px;
}

.scoped-bootstrap .btn-xs .badge,
.scoped-bootstrap .btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}

.scoped-bootstrap a.badge:hover,
.scoped-bootstrap a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}

.scoped-bootstrap .list-group-item.active > .badge,
.scoped-bootstrap .nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}

.scoped-bootstrap .list-group-item > .badge {
  float: right;
}

.scoped-bootstrap .list-group-item > .badge + .badge {
  margin-right: 5px;
}

.scoped-bootstrap .nav-pills > li > a > .badge {
  margin-left: 3px;
}

.scoped-bootstrap .jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eee;
}

.scoped-bootstrap .jumbotron h1,
.scoped-bootstrap .jumbotron .h1 {
  color: inherit;
}

.scoped-bootstrap .jumbotron p {
  margin-bottom: 15px;
  font-size: 21px;
  font-weight: 200;
}

.scoped-bootstrap .jumbotron > hr {
  border-top-color: #d5d5d5;
}

.scoped-bootstrap .container .jumbotron,
.scoped-bootstrap .container-fluid .jumbotron {
  padding-right: 15px;
  padding-left: 15px;
  border-radius: 6px;
}

.scoped-bootstrap .jumbotron .container {
  max-width: 100%;
}

@media screen and (min-width: 768px) {
  .scoped-bootstrap .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }

  .scoped-bootstrap .container .jumbotron,
  .scoped-bootstrap .container-fluid .jumbotron {
    padding-right: 60px;
    padding-left: 60px;
  }

  .scoped-bootstrap .jumbotron h1,
  .scoped-bootstrap .jumbotron .h1 {
    font-size: 63px;
  }
}

.scoped-bootstrap .thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 20px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  -webkit-transition: border .2s ease-in-out;
  -o-transition: border .2s ease-in-out;
  transition: border .2s ease-in-out;
}

.scoped-bootstrap .thumbnail > img,
.scoped-bootstrap .thumbnail a > img {
  margin-right: auto;
  margin-left: auto;
}

.scoped-bootstrap a.thumbnail:hover,
.scoped-bootstrap a.thumbnail:focus,
.scoped-bootstrap a.thumbnail.active {
  border-color: #337ab7;
}

.scoped-bootstrap .thumbnail .caption {
  padding: 9px;
  color: #333;
}

.scoped-bootstrap .alert {
  padding: 15px;
  margin-bottom: 20px;
  border: 1px solid transparent;
  border-radius: 4px;
}

.scoped-bootstrap .alert h4 {
  margin-top: 0;
  color: inherit;
}

.scoped-bootstrap .alert .alert-link {
  font-weight: bold;
}

.scoped-bootstrap .alert > p,
.scoped-bootstrap .alert > ul {
  margin-bottom: 0;
}

.scoped-bootstrap .alert > p + p {
  margin-top: 5px;
}

.scoped-bootstrap .alert-dismissable,
.scoped-bootstrap .alert-dismissible {
  padding-right: 35px;
}

.scoped-bootstrap .alert-dismissable .close,
.scoped-bootstrap .alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}

.scoped-bootstrap .alert-success {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}

.scoped-bootstrap .alert-success hr {
  border-top-color: #c9e2b3;
}

.scoped-bootstrap .alert-success .alert-link {
  color: #2b542c;
}

.scoped-bootstrap .alert-info {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}

.scoped-bootstrap .alert-info hr {
  border-top-color: #a6e1ec;
}

.scoped-bootstrap .alert-info .alert-link {
  color: #245269;
}

.scoped-bootstrap .alert-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}

.scoped-bootstrap .alert-warning hr {
  border-top-color: #f7e1b5;
}

.scoped-bootstrap .alert-warning .alert-link {
  color: #66512c;
}

.scoped-bootstrap .alert-danger {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}

.scoped-bootstrap .alert-danger hr {
  border-top-color: #e4b9c0;
}

.scoped-bootstrap .alert-danger .alert-link {
  color: #843534;
}

@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }

  to {
    background-position: 0 0;
  }
}

@-o-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }

  to {
    background-position: 0 0;
  }
}

@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }

  to {
    background-position: 0 0;
  }
}

.scoped-bootstrap .progress {
  height: 20px;
  margin-bottom: 20px;
  overflow: hidden;
  background-color: #f5f5f5;
  border-radius: 4px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, .1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, .1);
}

.scoped-bootstrap .progress-bar {
  float: left;
  width: 0;
  height: 100%;
  font-size: 12px;
  line-height: 20px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, .15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, .15);
  -webkit-transition: width .6s ease;
  -o-transition: width .6s ease;
  transition: width .6s ease;
}

.scoped-bootstrap .progress-striped .progress-bar,
.scoped-bootstrap .progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  -webkit-background-size: 40px 40px;
  background-size: 40px 40px;
}

.scoped-bootstrap .progress.active .progress-bar,
.scoped-bootstrap .progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}

.scoped-bootstrap .progress-bar-success {
  background-color: #5cb85c;
}

.scoped-bootstrap .progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
}

.scoped-bootstrap .progress-bar-info {
  background-color: #5bc0de;
}

.scoped-bootstrap .progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
}

.scoped-bootstrap .progress-bar-warning {
  background-color: #f0ad4e;
}

.scoped-bootstrap .progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
}

.scoped-bootstrap .progress-bar-danger {
  background-color: #d9534f;
}

.scoped-bootstrap .progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
}

.scoped-bootstrap .media {
  margin-top: 15px;
}

.scoped-bootstrap .media:first-child {
  margin-top: 0;
}

.scoped-bootstrap .media,
.scoped-bootstrap .media-body {
  overflow: hidden;
  zoom: 1;
}

.scoped-bootstrap .media-body {
  width: 10000px;
}

.scoped-bootstrap .media-object {
  display: block;
}

.scoped-bootstrap .media-object.img-thumbnail {
  max-width: none;
}

.scoped-bootstrap .media-right,
.scoped-bootstrap .media > .pull-right {
  padding-left: 10px;
}

.scoped-bootstrap .media-left,
.scoped-bootstrap .media > .pull-left {
  padding-right: 10px;
}

.scoped-bootstrap .media-left,
.scoped-bootstrap .media-right,
.scoped-bootstrap .media-body {
  display: table-cell;
  vertical-align: top;
}

.scoped-bootstrap .media-middle {
  vertical-align: middle;
}

.scoped-bootstrap .media-bottom {
  vertical-align: bottom;
}

.scoped-bootstrap .media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}

.scoped-bootstrap .media-list {
  padding-left: 0;
  list-style: none;
}

.scoped-bootstrap .list-group {
  padding-left: 0;
  margin-bottom: 20px;
}

.scoped-bootstrap .list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}

.scoped-bootstrap .list-group-item:first-child {
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}

.scoped-bootstrap .list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 4px;
  border-bottom-left-radius: 4px;
}

.scoped-bootstrap a.list-group-item,
.scoped-bootstrap button.list-group-item {
  color: #555;
}

.scoped-bootstrap a.list-group-item .list-group-item-heading,
.scoped-bootstrap button.list-group-item .list-group-item-heading {
  color: #333;
}

.scoped-bootstrap a.list-group-item:hover,
.scoped-bootstrap button.list-group-item:hover,
.scoped-bootstrap a.list-group-item:focus,
.scoped-bootstrap button.list-group-item:focus {
  color: #555;
  text-decoration: none;
  background-color: #f5f5f5;
}

.scoped-bootstrap button.list-group-item {
  width: 100%;
  text-align: left;
}

.scoped-bootstrap .list-group-item.disabled,
.scoped-bootstrap .list-group-item.disabled:hover,
.scoped-bootstrap .list-group-item.disabled:focus {
  color: #777;
  cursor: not-allowed;
  background-color: #eee;
}

.scoped-bootstrap .list-group-item.disabled .list-group-item-heading,
.scoped-bootstrap .list-group-item.disabled:hover .list-group-item-heading,
.scoped-bootstrap .list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}

.scoped-bootstrap .list-group-item.disabled .list-group-item-text,
.scoped-bootstrap .list-group-item.disabled:hover .list-group-item-text,
.scoped-bootstrap .list-group-item.disabled:focus .list-group-item-text {
  color: #777;
}

.scoped-bootstrap .list-group-item.active,
.scoped-bootstrap .list-group-item.active:hover,
.scoped-bootstrap .list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}

.scoped-bootstrap .list-group-item.active .list-group-item-heading,
.scoped-bootstrap .list-group-item.active:hover .list-group-item-heading,
.scoped-bootstrap .list-group-item.active:focus .list-group-item-heading,
.scoped-bootstrap .list-group-item.active .list-group-item-heading > small,
.scoped-bootstrap .list-group-item.active:hover .list-group-item-heading > small,
.scoped-bootstrap .list-group-item.active:focus .list-group-item-heading > small,
.scoped-bootstrap .list-group-item.active .list-group-item-heading > .small,
.scoped-bootstrap .list-group-item.active:hover .list-group-item-heading > .small,
.scoped-bootstrap .list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}

.scoped-bootstrap .list-group-item.active .list-group-item-text,
.scoped-bootstrap .list-group-item.active:hover .list-group-item-text,
.scoped-bootstrap .list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}

.scoped-bootstrap .list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}

.scoped-bootstrap a.list-group-item-success,
.scoped-bootstrap button.list-group-item-success {
  color: #3c763d;
}

.scoped-bootstrap a.list-group-item-success .list-group-item-heading,
.scoped-bootstrap button.list-group-item-success .list-group-item-heading {
  color: inherit;
}

.scoped-bootstrap a.list-group-item-success:hover,
.scoped-bootstrap button.list-group-item-success:hover,
.scoped-bootstrap a.list-group-item-success:focus,
.scoped-bootstrap button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}

.scoped-bootstrap a.list-group-item-success.active,
.scoped-bootstrap button.list-group-item-success.active,
.scoped-bootstrap a.list-group-item-success.active:hover,
.scoped-bootstrap button.list-group-item-success.active:hover,
.scoped-bootstrap a.list-group-item-success.active:focus,
.scoped-bootstrap button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}

.scoped-bootstrap .list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}

.scoped-bootstrap a.list-group-item-info,
.scoped-bootstrap button.list-group-item-info {
  color: #31708f;
}

.scoped-bootstrap a.list-group-item-info .list-group-item-heading,
.scoped-bootstrap button.list-group-item-info .list-group-item-heading {
  color: inherit;
}

.scoped-bootstrap a.list-group-item-info:hover,
.scoped-bootstrap button.list-group-item-info:hover,
.scoped-bootstrap a.list-group-item-info:focus,
.scoped-bootstrap button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}

.scoped-bootstrap a.list-group-item-info.active,
.scoped-bootstrap button.list-group-item-info.active,
.scoped-bootstrap a.list-group-item-info.active:hover,
.scoped-bootstrap button.list-group-item-info.active:hover,
.scoped-bootstrap a.list-group-item-info.active:focus,
.scoped-bootstrap button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}

.scoped-bootstrap .list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}

.scoped-bootstrap a.list-group-item-warning,
.scoped-bootstrap button.list-group-item-warning {
  color: #8a6d3b;
}

.scoped-bootstrap a.list-group-item-warning .list-group-item-heading,
.scoped-bootstrap button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}

.scoped-bootstrap a.list-group-item-warning:hover,
.scoped-bootstrap button.list-group-item-warning:hover,
.scoped-bootstrap a.list-group-item-warning:focus,
.scoped-bootstrap button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}

.scoped-bootstrap a.list-group-item-warning.active,
.scoped-bootstrap button.list-group-item-warning.active,
.scoped-bootstrap a.list-group-item-warning.active:hover,
.scoped-bootstrap button.list-group-item-warning.active:hover,
.scoped-bootstrap a.list-group-item-warning.active:focus,
.scoped-bootstrap button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}

.scoped-bootstrap .list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}

.scoped-bootstrap a.list-group-item-danger,
.scoped-bootstrap button.list-group-item-danger {
  color: #a94442;
}

.scoped-bootstrap a.list-group-item-danger .list-group-item-heading,
.scoped-bootstrap button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}

.scoped-bootstrap a.list-group-item-danger:hover,
.scoped-bootstrap button.list-group-item-danger:hover,
.scoped-bootstrap a.list-group-item-danger:focus,
.scoped-bootstrap button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}

.scoped-bootstrap a.list-group-item-danger.active,
.scoped-bootstrap button.list-group-item-danger.active,
.scoped-bootstrap a.list-group-item-danger.active:hover,
.scoped-bootstrap button.list-group-item-danger.active:hover,
.scoped-bootstrap a.list-group-item-danger.active:focus,
.scoped-bootstrap button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}

.scoped-bootstrap .list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}

.scoped-bootstrap .list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}

.scoped-bootstrap .panel {
  margin-bottom: 20px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 4px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
}

.scoped-bootstrap .panel-body {
  padding: 15px;
}

.scoped-bootstrap .panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}

.scoped-bootstrap .panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}

.scoped-bootstrap .panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 16px;
  color: inherit;
}

.scoped-bootstrap .panel-title > a,
.scoped-bootstrap .panel-title > small,
.scoped-bootstrap .panel-title > .small,
.scoped-bootstrap .panel-title > small > a,
.scoped-bootstrap .panel-title > .small > a {
  color: inherit;
}

.scoped-bootstrap .panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 3px;
  border-bottom-left-radius: 3px;
}

.scoped-bootstrap .panel > .list-group,
.scoped-bootstrap .panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}

.scoped-bootstrap .panel > .list-group .list-group-item,
.scoped-bootstrap .panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}

.scoped-bootstrap .panel > .list-group:first-child .list-group-item:first-child,
.scoped-bootstrap .panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}

.scoped-bootstrap .panel > .list-group:last-child .list-group-item:last-child,
.scoped-bootstrap .panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 3px;
  border-bottom-left-radius: 3px;
}

.scoped-bootstrap .panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.scoped-bootstrap .panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}

.scoped-bootstrap .list-group + .panel-footer {
  border-top-width: 0;
}

.scoped-bootstrap .panel > .table,
.scoped-bootstrap .panel > .table-responsive > .table,
.scoped-bootstrap .panel > .panel-collapse > .table {
  margin-bottom: 0;
}

.scoped-bootstrap .panel > .table caption,
.scoped-bootstrap .panel > .table-responsive > .table caption,
.scoped-bootstrap .panel > .panel-collapse > .table caption {
  padding-right: 15px;
  padding-left: 15px;
}

.scoped-bootstrap .panel > .table:first-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child {
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}

.scoped-bootstrap .panel > .table:first-child > thead:first-child > tr:first-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.scoped-bootstrap .panel > .table:first-child > tbody:first-child > tr:first-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}

.scoped-bootstrap .panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.scoped-bootstrap .panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.scoped-bootstrap .panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.scoped-bootstrap .panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 3px;
}

.scoped-bootstrap .panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.scoped-bootstrap .panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.scoped-bootstrap .panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.scoped-bootstrap .panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.scoped-bootstrap .panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 3px;
}

.scoped-bootstrap .panel > .table:last-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 3px;
  border-bottom-left-radius: 3px;
}

.scoped-bootstrap .panel > .table:last-child > tbody:last-child > tr:last-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.scoped-bootstrap .panel > .table:last-child > tfoot:last-child > tr:last-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-right-radius: 3px;
  border-bottom-left-radius: 3px;
}

.scoped-bootstrap .panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.scoped-bootstrap .panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.scoped-bootstrap .panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.scoped-bootstrap .panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 3px;
}

.scoped-bootstrap .panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.scoped-bootstrap .panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.scoped-bootstrap .panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.scoped-bootstrap .panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.scoped-bootstrap .panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 3px;
}

.scoped-bootstrap .panel > .panel-body + .table,
.scoped-bootstrap .panel > .panel-body + .table-responsive,
.scoped-bootstrap .panel > .table + .panel-body,
.scoped-bootstrap .panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}

.scoped-bootstrap .panel > .table > tbody:first-child > tr:first-child th,
.scoped-bootstrap .panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}

.scoped-bootstrap .panel > .table-bordered,
.scoped-bootstrap .panel > .table-responsive > .table-bordered {
  border: 0;
}

.scoped-bootstrap .panel > .table-bordered > thead > tr > th:first-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.scoped-bootstrap .panel > .table-bordered > tbody > tr > th:first-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.scoped-bootstrap .panel > .table-bordered > tfoot > tr > th:first-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.scoped-bootstrap .panel > .table-bordered > thead > tr > td:first-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.scoped-bootstrap .panel > .table-bordered > tbody > tr > td:first-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.scoped-bootstrap .panel > .table-bordered > tfoot > tr > td:first-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}

.scoped-bootstrap .panel > .table-bordered > thead > tr > th:last-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.scoped-bootstrap .panel > .table-bordered > tbody > tr > th:last-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.scoped-bootstrap .panel > .table-bordered > tfoot > tr > th:last-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.scoped-bootstrap .panel > .table-bordered > thead > tr > td:last-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.scoped-bootstrap .panel > .table-bordered > tbody > tr > td:last-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.scoped-bootstrap .panel > .table-bordered > tfoot > tr > td:last-child,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}

.scoped-bootstrap .panel > .table-bordered > thead > tr:first-child > td,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.scoped-bootstrap .panel > .table-bordered > tbody > tr:first-child > td,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.scoped-bootstrap .panel > .table-bordered > thead > tr:first-child > th,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.scoped-bootstrap .panel > .table-bordered > tbody > tr:first-child > th,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}

.scoped-bootstrap .panel > .table-bordered > tbody > tr:last-child > td,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.scoped-bootstrap .panel > .table-bordered > tfoot > tr:last-child > td,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.scoped-bootstrap .panel > .table-bordered > tbody > tr:last-child > th,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.scoped-bootstrap .panel > .table-bordered > tfoot > tr:last-child > th,
.scoped-bootstrap .panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}

.scoped-bootstrap .panel > .table-responsive {
  margin-bottom: 0;
  border: 0;
}

.scoped-bootstrap .panel-group {
  margin-bottom: 20px;
}

.scoped-bootstrap .panel-group .panel {
  margin-bottom: 0;
  border-radius: 4px;
}

.scoped-bootstrap .panel-group .panel + .panel {
  margin-top: 5px;
}

.scoped-bootstrap .panel-group .panel-heading {
  border-bottom: 0;
}

.scoped-bootstrap .panel-group .panel-heading + .panel-collapse > .panel-body,
.scoped-bootstrap .panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}

.scoped-bootstrap .panel-group .panel-footer {
  border-top: 0;
}

.scoped-bootstrap .panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}

.scoped-bootstrap .panel-default {
  border-color: #ddd;
}

.scoped-bootstrap .panel-default > .panel-heading {
  color: #333;
  background-color: #f5f5f5;
  border-color: #ddd;
}

.scoped-bootstrap .panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}

.scoped-bootstrap .panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333;
}

.scoped-bootstrap .panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}

.scoped-bootstrap .panel-primary {
  border-color: #337ab7;
}

.scoped-bootstrap .panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}

.scoped-bootstrap .panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}

.scoped-bootstrap .panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}

.scoped-bootstrap .panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}

.scoped-bootstrap .panel-success {
  border-color: #d6e9c6;
}

.scoped-bootstrap .panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}

.scoped-bootstrap .panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}

.scoped-bootstrap .panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}

.scoped-bootstrap .panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}

.scoped-bootstrap .panel-info {
  border-color: #bce8f1;
}

.scoped-bootstrap .panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}

.scoped-bootstrap .panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}

.scoped-bootstrap .panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}

.scoped-bootstrap .panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}

.scoped-bootstrap .panel-warning {
  border-color: #faebcc;
}

.scoped-bootstrap .panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}

.scoped-bootstrap .panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}

.scoped-bootstrap .panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}

.scoped-bootstrap .panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}

.scoped-bootstrap .panel-danger {
  border-color: #ebccd1;
}

.scoped-bootstrap .panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}

.scoped-bootstrap .panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}

.scoped-bootstrap .panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}

.scoped-bootstrap .panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}

.scoped-bootstrap .embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}

.scoped-bootstrap .embed-responsive .embed-responsive-item,
.scoped-bootstrap .embed-responsive iframe,
.scoped-bootstrap .embed-responsive embed,
.scoped-bootstrap .embed-responsive object,
.scoped-bootstrap .embed-responsive video {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.scoped-bootstrap .embed-responsive-16by9 {
  padding-bottom: 56.25%;
}

.scoped-bootstrap .embed-responsive-4by3 {
  padding-bottom: 75%;
}

.scoped-bootstrap .well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 4px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, .05);
}

.scoped-bootstrap .well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, .15);
}

.scoped-bootstrap .well-lg {
  padding: 24px;
  border-radius: 6px;
}

.scoped-bootstrap .well-sm {
  padding: 9px;
  border-radius: 3px;
}

.scoped-bootstrap .close {
  float: right;
  font-size: 21px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  filter: alpha(opacity=20);
  opacity: .2;
}

.scoped-bootstrap .close:hover,
.scoped-bootstrap .close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  filter: alpha(opacity=50);
  opacity: .5;
}

.scoped-bootstrap button.close {
  -webkit-appearance: none;
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
}

.scoped-bootstrap .modal-open {
  overflow: hidden;
}

.scoped-bootstrap .modal {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  display: none;
  overflow: hidden;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}

.scoped-bootstrap .modal.fade .modal-dialog {
  -webkit-transition: -webkit-transform .3s ease-out;
  -o-transition: -o-transform .3s ease-out;
  transition: transform .3s ease-out;
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
}

.scoped-bootstrap .modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}

.scoped-bootstrap .modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}

.scoped-bootstrap .modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}

.scoped-bootstrap .modal-content {
  position: relative;
  background-color: #fff;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, .2);
  border-radius: 6px;
  outline: 0;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, .5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, .5);
}

.scoped-bootstrap .modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}

.scoped-bootstrap .modal-backdrop.fade {
  filter: alpha(opacity=0);
  opacity: 0;
}

.scoped-bootstrap .modal-backdrop.in {
  filter: alpha(opacity=50);
  opacity: .5;
}

.scoped-bootstrap .modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}

.scoped-bootstrap .modal-header .close {
  margin-top: -2px;
}

.scoped-bootstrap .modal-title {
  margin: 0;
  line-height: 1.42857143;
}

.scoped-bootstrap .modal-body {
  position: relative;
  padding: 15px;
}

.scoped-bootstrap .modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}

.scoped-bootstrap .modal-footer .btn + .btn {
  margin-bottom: 0;
  margin-left: 5px;
}

.scoped-bootstrap .modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}

.scoped-bootstrap .modal-footer .btn-block + .btn-block {
  margin-left: 0;
}

.scoped-bootstrap .modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}

@media (min-width: 768px) {
  .scoped-bootstrap .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }

  .scoped-bootstrap .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, .5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, .5);
  }

  .scoped-bootstrap .modal-sm {
    width: 300px;
  }
}

@media (min-width: 992px) {
  .scoped-bootstrap .modal-lg {
    width: 900px;
  }
}

.scoped-bootstrap .tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 12px;
  font-style: normal;
  font-weight: normal;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  white-space: normal;
  filter: alpha(opacity=0);
  opacity: 0;
  line-break: auto;
}

.scoped-bootstrap .tooltip.in {
  filter: alpha(opacity=90);
  opacity: .9;
}

.scoped-bootstrap .tooltip.top {
  padding: 5px 0;
  margin-top: -3px;
}

.scoped-bootstrap .tooltip.right {
  padding: 0 5px;
  margin-left: 3px;
}

.scoped-bootstrap .tooltip.bottom {
  padding: 5px 0;
  margin-top: 3px;
}

.scoped-bootstrap .tooltip.left {
  padding: 0 5px;
  margin-left: -3px;
}

.scoped-bootstrap .tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 4px;
}

.scoped-bootstrap .tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}

.scoped-bootstrap .tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}

.scoped-bootstrap .tooltip.top-left .tooltip-arrow {
  right: 5px;
  bottom: 0;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}

.scoped-bootstrap .tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}

.scoped-bootstrap .tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}

.scoped-bootstrap .tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}

.scoped-bootstrap .tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}

.scoped-bootstrap .tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}

.scoped-bootstrap .tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}

.scoped-bootstrap .popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  font-style: normal;
  font-weight: normal;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  white-space: normal;
  background-color: #fff;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, .2);
  border-radius: 6px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, .2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, .2);
  line-break: auto;
}

.scoped-bootstrap .popover.top {
  margin-top: -10px;
}

.scoped-bootstrap .popover.right {
  margin-left: 10px;
}

.scoped-bootstrap .popover.bottom {
  margin-top: 10px;
}

.scoped-bootstrap .popover.left {
  margin-left: -10px;
}

.scoped-bootstrap .popover-title {
  padding: 8px 14px;
  margin: 0;
  font-size: 14px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 5px 5px 0 0;
}

.scoped-bootstrap .popover-content {
  padding: 9px 14px;
}

.scoped-bootstrap .popover > .arrow,
.scoped-bootstrap .popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}

.scoped-bootstrap .popover > .arrow {
  border-width: 11px;
}

.scoped-bootstrap .popover > .arrow:after {
  content: "";
  border-width: 10px;
}

.scoped-bootstrap .popover.top > .arrow {
  bottom: -11px;
  left: 50%;
  margin-left: -11px;
  border-top-color: #999;
  border-top-color: rgba(0, 0, 0, .25);
  border-bottom-width: 0;
}

.scoped-bootstrap .popover.top > .arrow:after {
  bottom: 1px;
  margin-left: -10px;
  content: " ";
  border-top-color: #fff;
  border-bottom-width: 0;
}

.scoped-bootstrap .popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-right-color: #999;
  border-right-color: rgba(0, 0, 0, .25);
  border-left-width: 0;
}

.scoped-bootstrap .popover.right > .arrow:after {
  bottom: -10px;
  left: 1px;
  content: " ";
  border-right-color: #fff;
  border-left-width: 0;
}

.scoped-bootstrap .popover.bottom > .arrow {
  top: -11px;
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999;
  border-bottom-color: rgba(0, 0, 0, .25);
}

.scoped-bootstrap .popover.bottom > .arrow:after {
  top: 1px;
  margin-left: -10px;
  content: " ";
  border-top-width: 0;
  border-bottom-color: #fff;
}

.scoped-bootstrap .popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999;
  border-left-color: rgba(0, 0, 0, .25);
}

.scoped-bootstrap .popover.left > .arrow:after {
  right: 1px;
  bottom: -10px;
  content: " ";
  border-right-width: 0;
  border-left-color: #fff;
}

.scoped-bootstrap .carousel {
  position: relative;
}

.scoped-bootstrap .carousel-inner {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.scoped-bootstrap .carousel-inner > .item {
  position: relative;
  display: none;
  -webkit-transition: .6s ease-in-out left;
  -o-transition: .6s ease-in-out left;
  transition: .6s ease-in-out left;
}

.scoped-bootstrap .carousel-inner > .item > img,
.scoped-bootstrap .carousel-inner > .item > a > img {
  line-height: 1;
}

@media all and (transform-3d), (-webkit-transform-3d) {
  .scoped-bootstrap .carousel-inner > .item {
    -webkit-transition: -webkit-transform .6s ease-in-out;
    -o-transition: -o-transform .6s ease-in-out;
    transition: transform .6s ease-in-out;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    perspective: 1000px;
  }

  .scoped-bootstrap .carousel-inner > .item.next,
  .scoped-bootstrap .carousel-inner > .item.active.right {
    left: 0;
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
  }

  .scoped-bootstrap .carousel-inner > .item.prev,
  .scoped-bootstrap .carousel-inner > .item.active.left {
    left: 0;
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
  }

  .scoped-bootstrap .carousel-inner > .item.next.left,
  .scoped-bootstrap .carousel-inner > .item.prev.right,
  .scoped-bootstrap .carousel-inner > .item.active {
    left: 0;
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }
}

.scoped-bootstrap .carousel-inner > .active,
.scoped-bootstrap .carousel-inner > .next,
.scoped-bootstrap .carousel-inner > .prev {
  display: block;
}

.scoped-bootstrap .carousel-inner > .active {
  left: 0;
}

.scoped-bootstrap .carousel-inner > .next,
.scoped-bootstrap .carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}

.scoped-bootstrap .carousel-inner > .next {
  left: 100%;
}

.scoped-bootstrap .carousel-inner > .prev {
  left: -100%;
}

.scoped-bootstrap .carousel-inner > .next.left,
.scoped-bootstrap .carousel-inner > .prev.right {
  left: 0;
}

.scoped-bootstrap .carousel-inner > .active.left {
  left: -100%;
}

.scoped-bootstrap .carousel-inner > .active.right {
  left: 100%;
}

.scoped-bootstrap .carousel-control {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 15%;
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, .6);
  background-color: rgba(0, 0, 0, 0);
  filter: alpha(opacity=50);
  opacity: .5;
}

.scoped-bootstrap .carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, .5) 0%, rgba(0, 0, 0, .0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, .5) 0%, rgba(0, 0, 0, .0001) 100%);
  background-image: -webkit-gradient(linear, left top, right top, from(rgba(0, 0, 0, .5)), to(rgba(0, 0, 0, .0001)));
  background-image: linear-gradient(to right, rgba(0, 0, 0, .5) 0%, rgba(0, 0, 0, .0001) 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
  background-repeat: repeat-x;
}

.scoped-bootstrap .carousel-control.right {
  right: 0;
  left: auto;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, .0001) 0%, rgba(0, 0, 0, .5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, .0001) 0%, rgba(0, 0, 0, .5) 100%);
  background-image: -webkit-gradient(linear, left top, right top, from(rgba(0, 0, 0, .0001)), to(rgba(0, 0, 0, .5)));
  background-image: linear-gradient(to right, rgba(0, 0, 0, .0001) 0%, rgba(0, 0, 0, .5) 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
  background-repeat: repeat-x;
}

.scoped-bootstrap .carousel-control:hover,
.scoped-bootstrap .carousel-control:focus {
  color: #fff;
  text-decoration: none;
  filter: alpha(opacity=90);
  outline: 0;
  opacity: .9;
}

.scoped-bootstrap .carousel-control .icon-prev,
.scoped-bootstrap .carousel-control .icon-next,
.scoped-bootstrap .carousel-control .glyphicon-chevron-left,
.scoped-bootstrap .carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  z-index: 5;
  display: inline-block;
  margin-top: -10px;
}

.scoped-bootstrap .carousel-control .icon-prev,
.scoped-bootstrap .carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}

.scoped-bootstrap .carousel-control .icon-next,
.scoped-bootstrap .carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}

.scoped-bootstrap .carousel-control .icon-prev,
.scoped-bootstrap .carousel-control .icon-next {
  width: 20px;
  height: 20px;
  font-family: serif;
  line-height: 1;
}

.scoped-bootstrap .carousel-control .icon-prev:before {
  content: '\2039';
}

.scoped-bootstrap .carousel-control .icon-next:before {
  content: '\203A';
}

.scoped-bootstrap .carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  padding-left: 0;
  margin-left: -30%;
  text-align: center;
  list-style: none;
}

.scoped-bootstrap .carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
  border: 1px solid #fff;
  border-radius: 10px;
}

.scoped-bootstrap .carousel-indicators .active {
  width: 12px;
  height: 12px;
  margin: 0;
  background-color: #fff;
}

.scoped-bootstrap .carousel-caption {
  position: absolute;
  right: 15%;
  bottom: 20px;
  left: 15%;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, .6);
}

.scoped-bootstrap .carousel-caption .btn {
  text-shadow: none;
}

@media screen and (min-width: 768px) {
  .scoped-bootstrap .carousel-control .glyphicon-chevron-left,
  .scoped-bootstrap .carousel-control .glyphicon-chevron-right,
  .scoped-bootstrap .carousel-control .icon-prev,
  .scoped-bootstrap .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }

  .scoped-bootstrap .carousel-control .glyphicon-chevron-left,
  .scoped-bootstrap .carousel-control .icon-prev {
    margin-left: -10px;
  }

  .scoped-bootstrap .carousel-control .glyphicon-chevron-right,
  .scoped-bootstrap .carousel-control .icon-next {
    margin-right: -10px;
  }

  .scoped-bootstrap .carousel-caption {
    right: 20%;
    left: 20%;
    padding-bottom: 30px;
  }

  .scoped-bootstrap .carousel-indicators {
    bottom: 20px;
  }
}

.scoped-bootstrap .clearfix:before,
.scoped-bootstrap .clearfix:after,
.scoped-bootstrap .dl-horizontal dd:before,
.scoped-bootstrap .dl-horizontal dd:after,
.scoped-bootstrap .container:before,
.scoped-bootstrap .container:after,
.scoped-bootstrap .container-fluid:before,
.scoped-bootstrap .container-fluid:after,
.scoped-bootstrap .row:before,
.scoped-bootstrap .row:after,
.scoped-bootstrap .form-horizontal .form-group:before,
.scoped-bootstrap .form-horizontal .form-group:after,
.scoped-bootstrap .btn-toolbar:before,
.scoped-bootstrap .btn-toolbar:after,
.scoped-bootstrap .btn-group-vertical > .btn-group:before,
.scoped-bootstrap .btn-group-vertical > .btn-group:after,
.scoped-bootstrap .nav:before,
.scoped-bootstrap .nav:after,
.scoped-bootstrap .navbar:before,
.scoped-bootstrap .navbar:after,
.scoped-bootstrap .navbar-header:before,
.scoped-bootstrap .navbar-header:after,
.scoped-bootstrap .navbar-collapse:before,
.scoped-bootstrap .navbar-collapse:after,
.scoped-bootstrap .pager:before,
.scoped-bootstrap .pager:after,
.scoped-bootstrap .panel-body:before,
.scoped-bootstrap .panel-body:after,
.scoped-bootstrap .modal-header:before,
.scoped-bootstrap .modal-header:after,
.scoped-bootstrap .modal-footer:before,
.scoped-bootstrap .modal-footer:after {
  display: table;
  content: " ";
}

.scoped-bootstrap .clearfix:after,
.scoped-bootstrap .dl-horizontal dd:after,
.scoped-bootstrap .container:after,
.scoped-bootstrap .container-fluid:after,
.scoped-bootstrap .row:after,
.scoped-bootstrap .form-horizontal .form-group:after,
.scoped-bootstrap .btn-toolbar:after,
.scoped-bootstrap .btn-group-vertical > .btn-group:after,
.scoped-bootstrap .nav:after,
.scoped-bootstrap .navbar:after,
.scoped-bootstrap .navbar-header:after,
.scoped-bootstrap .navbar-collapse:after,
.scoped-bootstrap .pager:after,
.scoped-bootstrap .panel-body:after,
.scoped-bootstrap .modal-header:after,
.scoped-bootstrap .modal-footer:after {
  clear: both;
}

.scoped-bootstrap .center-block {
  display: block;
  margin-right: auto;
  margin-left: auto;
}

.scoped-bootstrap .pull-right {
  float: right !important;
}

.scoped-bootstrap .pull-left {
  float: left !important;
}

.scoped-bootstrap .hide {
  display: none !important;
}

.scoped-bootstrap .show {
  display: block !important;
}

.scoped-bootstrap .invisible {
  visibility: hidden;
}

.scoped-bootstrap .text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}

.scoped-bootstrap .hidden {
  display: none !important;
}

.scoped-bootstrap .affix {
  position: fixed;
}

@-ms-viewport {
  width: device-width;
}

.scoped-bootstrap .visible-xs,
.scoped-bootstrap .visible-sm,
.scoped-bootstrap .visible-md,
.scoped-bootstrap .visible-lg {
  display: none !important;
}

.scoped-bootstrap .visible-xs-block,
.scoped-bootstrap .visible-xs-inline,
.scoped-bootstrap .visible-xs-inline-block,
.scoped-bootstrap .visible-sm-block,
.scoped-bootstrap .visible-sm-inline,
.scoped-bootstrap .visible-sm-inline-block,
.scoped-bootstrap .visible-md-block,
.scoped-bootstrap .visible-md-inline,
.scoped-bootstrap .visible-md-inline-block,
.scoped-bootstrap .visible-lg-block,
.scoped-bootstrap .visible-lg-inline,
.scoped-bootstrap .visible-lg-inline-block {
  display: none !important;
}

@media (max-width: 767px) {
  .scoped-bootstrap .visible-xs {
    display: block !important;
  }

  .scoped-bootstrap table.visible-xs {
    display: table !important;
  }

  .scoped-bootstrap tr.visible-xs {
    display: table-row !important;
  }

  .scoped-bootstrap th.visible-xs,
  .scoped-bootstrap td.visible-xs {
    display: table-cell !important;
  }
}

@media (max-width: 767px) {
  .scoped-bootstrap .visible-xs-block {
    display: block !important;
  }
}

@media (max-width: 767px) {
  .scoped-bootstrap .visible-xs-inline {
    display: inline !important;
  }
}

@media (max-width: 767px) {
  .scoped-bootstrap .visible-xs-inline-block {
    display: inline-block !important;
  }
}

@media (min-width: 768px) and (max-width: 991px) {
  .scoped-bootstrap .visible-sm {
    display: block !important;
  }

  .scoped-bootstrap table.visible-sm {
    display: table !important;
  }

  .scoped-bootstrap tr.visible-sm {
    display: table-row !important;
  }

  .scoped-bootstrap th.visible-sm,
  .scoped-bootstrap td.visible-sm {
    display: table-cell !important;
  }
}

@media (min-width: 768px) and (max-width: 991px) {
  .scoped-bootstrap .visible-sm-block {
    display: block !important;
  }
}

@media (min-width: 768px) and (max-width: 991px) {
  .scoped-bootstrap .visible-sm-inline {
    display: inline !important;
  }
}

@media (min-width: 768px) and (max-width: 991px) {
  .scoped-bootstrap .visible-sm-inline-block {
    display: inline-block !important;
  }
}

@media (min-width: 992px) and (max-width: 1199px) {
  .scoped-bootstrap .visible-md {
    display: block !important;
  }

  .scoped-bootstrap table.visible-md {
    display: table !important;
  }

  .scoped-bootstrap tr.visible-md {
    display: table-row !important;
  }

  .scoped-bootstrap th.visible-md,
  .scoped-bootstrap td.visible-md {
    display: table-cell !important;
  }
}

@media (min-width: 992px) and (max-width: 1199px) {
  .scoped-bootstrap .visible-md-block {
    display: block !important;
  }
}

@media (min-width: 992px) and (max-width: 1199px) {
  .scoped-bootstrap .visible-md-inline {
    display: inline !important;
  }
}

@media (min-width: 992px) and (max-width: 1199px) {
  .scoped-bootstrap .visible-md-inline-block {
    display: inline-block !important;
  }
}

@media (min-width: 1200px) {
  .scoped-bootstrap .visible-lg {
    display: block !important;
  }

  .scoped-bootstrap table.visible-lg {
    display: table !important;
  }

  .scoped-bootstrap tr.visible-lg {
    display: table-row !important;
  }

  .scoped-bootstrap th.visible-lg,
  .scoped-bootstrap td.visible-lg {
    display: table-cell !important;
  }
}

@media (min-width: 1200px) {
  .scoped-bootstrap .visible-lg-block {
    display: block !important;
  }
}

@media (min-width: 1200px) {
  .scoped-bootstrap .visible-lg-inline {
    display: inline !important;
  }
}

@media (min-width: 1200px) {
  .scoped-bootstrap .visible-lg-inline-block {
    display: inline-block !important;
  }
}

@media (max-width: 767px) {
  .scoped-bootstrap .hidden-xs {
    display: none !important;
  }
}

@media (min-width: 768px) and (max-width: 991px) {
  .scoped-bootstrap .hidden-sm {
    display: none !important;
  }
}

@media (min-width: 992px) and (max-width: 1199px) {
  .scoped-bootstrap .hidden-md {
    display: none !important;
  }
}

@media (min-width: 1200px) {
  .scoped-bootstrap .hidden-lg {
    display: none !important;
  }
}

.scoped-bootstrap .visible-print {
  display: none !important;
}

@media print {
  .scoped-bootstrap .visible-print {
    display: block !important;
  }

  .scoped-bootstrap table.visible-print {
    display: table !important;
  }

  .scoped-bootstrap tr.visible-print {
    display: table-row !important;
  }

  .scoped-bootstrap th.visible-print,
  .scoped-bootstrap td.visible-print {
    display: table-cell !important;
  }
}

.scoped-bootstrap .visible-print-block {
  display: none !important;
}

@media print {
  .scoped-bootstrap .visible-print-block {
    display: block !important;
  }
}

.scoped-bootstrap .visible-print-inline {
  display: none !important;
}

@media print {
  .scoped-bootstrap .visible-print-inline {
    display: inline !important;
  }
}

.scoped-bootstrap .visible-print-inline-block {
  display: none !important;
}

@media print {
  .scoped-bootstrap .visible-print-inline-block {
    display: inline-block !important;
  }
}

@media print {
  .scoped-bootstrap .hidden-print {
    display: none !important;
  }
}
</style><style type="text/css">/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
.btn-default,
.btn-primary,
.btn-success,
.btn-info,
.btn-warning,
.btn-danger {
  text-shadow: 0 -1px 0 rgba(0, 0, 0, .2);
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .15), 0 1px 1px rgba(0, 0, 0, .075);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, .15), 0 1px 1px rgba(0, 0, 0, .075);
}
.btn-default:active,
.btn-primary:active,
.btn-success:active,
.btn-info:active,
.btn-warning:active,
.btn-danger:active,
.btn-default.active,
.btn-primary.active,
.btn-success.active,
.btn-info.active,
.btn-warning.active,
.btn-danger.active {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
          box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
}
.btn-default.disabled,
.btn-primary.disabled,
.btn-success.disabled,
.btn-info.disabled,
.btn-warning.disabled,
.btn-danger.disabled,
.btn-default[disabled],
.btn-primary[disabled],
.btn-success[disabled],
.btn-info[disabled],
.btn-warning[disabled],
.btn-danger[disabled],
fieldset[disabled] .btn-default,
fieldset[disabled] .btn-primary,
fieldset[disabled] .btn-success,
fieldset[disabled] .btn-info,
fieldset[disabled] .btn-warning,
fieldset[disabled] .btn-danger {
  -webkit-box-shadow: none;
          box-shadow: none;
}
.btn-default .badge,
.btn-primary .badge,
.btn-success .badge,
.btn-info .badge,
.btn-warning .badge,
.btn-danger .badge {
  text-shadow: none;
}
.btn:active,
.btn.active {
  background-image: none;
}
.btn-default {
  text-shadow: 0 1px 0 #fff;
  background-image: -webkit-linear-gradient(top, #fff 0%, #e0e0e0 100%);
  background-image:      -o-linear-gradient(top, #fff 0%, #e0e0e0 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#fff), to(#e0e0e0));
  background-image:         linear-gradient(to bottom, #fff 0%, #e0e0e0 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#ffe0e0e0', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #dbdbdb;
  border-color: #ccc;
}
.btn-default:hover,
.btn-default:focus {
  background-color: #e0e0e0;
  background-position: 0 -15px;
}
.btn-default:active,
.btn-default.active {
  background-color: #e0e0e0;
  border-color: #dbdbdb;
}
.btn-default.disabled,
.btn-default[disabled],
fieldset[disabled] .btn-default,
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus,
.btn-default.disabled:active,
.btn-default[disabled]:active,
fieldset[disabled] .btn-default:active,
.btn-default.disabled.active,
.btn-default[disabled].active,
fieldset[disabled] .btn-default.active {
  background-color: #e0e0e0;
  background-image: none;
}
.btn-primary {
  background-image: -webkit-linear-gradient(top, #337ab7 0%, #265a88 100%);
  background-image:      -o-linear-gradient(top, #337ab7 0%, #265a88 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#337ab7), to(#265a88));
  background-image:         linear-gradient(to bottom, #337ab7 0%, #265a88 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff337ab7', endColorstr='#ff265a88', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #245580;
}
.btn-primary:hover,
.btn-primary:focus {
  background-color: #265a88;
  background-position: 0 -15px;
}
.btn-primary:active,
.btn-primary.active {
  background-color: #265a88;
  border-color: #245580;
}
.btn-primary.disabled,
.btn-primary[disabled],
fieldset[disabled] .btn-primary,
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus,
.btn-primary.disabled:active,
.btn-primary[disabled]:active,
fieldset[disabled] .btn-primary:active,
.btn-primary.disabled.active,
.btn-primary[disabled].active,
fieldset[disabled] .btn-primary.active {
  background-color: #265a88;
  background-image: none;
}
.btn-success {
  background-image: -webkit-linear-gradient(top, #5cb85c 0%, #419641 100%);
  background-image:      -o-linear-gradient(top, #5cb85c 0%, #419641 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#5cb85c), to(#419641));
  background-image:         linear-gradient(to bottom, #5cb85c 0%, #419641 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5cb85c', endColorstr='#ff419641', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #3e8f3e;
}
.btn-success:hover,
.btn-success:focus {
  background-color: #419641;
  background-position: 0 -15px;
}
.btn-success:active,
.btn-success.active {
  background-color: #419641;
  border-color: #3e8f3e;
}
.btn-success.disabled,
.btn-success[disabled],
fieldset[disabled] .btn-success,
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus,
.btn-success.disabled:active,
.btn-success[disabled]:active,
fieldset[disabled] .btn-success:active,
.btn-success.disabled.active,
.btn-success[disabled].active,
fieldset[disabled] .btn-success.active {
  background-color: #419641;
  background-image: none;
}
.btn-info {
  background-image: -webkit-linear-gradient(top, #5bc0de 0%, #2aabd2 100%);
  background-image:      -o-linear-gradient(top, #5bc0de 0%, #2aabd2 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#5bc0de), to(#2aabd2));
  background-image:         linear-gradient(to bottom, #5bc0de 0%, #2aabd2 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff2aabd2', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #28a4c9;
}
.btn-info:hover,
.btn-info:focus {
  background-color: #2aabd2;
  background-position: 0 -15px;
}
.btn-info:active,
.btn-info.active {
  background-color: #2aabd2;
  border-color: #28a4c9;
}
.btn-info.disabled,
.btn-info[disabled],
fieldset[disabled] .btn-info,
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus,
.btn-info.disabled:active,
.btn-info[disabled]:active,
fieldset[disabled] .btn-info:active,
.btn-info.disabled.active,
.btn-info[disabled].active,
fieldset[disabled] .btn-info.active {
  background-color: #2aabd2;
  background-image: none;
}
.btn-warning {
  background-image: -webkit-linear-gradient(top, #f0ad4e 0%, #eb9316 100%);
  background-image:      -o-linear-gradient(top, #f0ad4e 0%, #eb9316 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f0ad4e), to(#eb9316));
  background-image:         linear-gradient(to bottom, #f0ad4e 0%, #eb9316 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff0ad4e', endColorstr='#ffeb9316', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #e38d13;
}
.btn-warning:hover,
.btn-warning:focus {
  background-color: #eb9316;
  background-position: 0 -15px;
}
.btn-warning:active,
.btn-warning.active {
  background-color: #eb9316;
  border-color: #e38d13;
}
.btn-warning.disabled,
.btn-warning[disabled],
fieldset[disabled] .btn-warning,
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus,
.btn-warning.disabled:active,
.btn-warning[disabled]:active,
fieldset[disabled] .btn-warning:active,
.btn-warning.disabled.active,
.btn-warning[disabled].active,
fieldset[disabled] .btn-warning.active {
  background-color: #eb9316;
  background-image: none;
}
.btn-danger {
  background-image: -webkit-linear-gradient(top, #d9534f 0%, #c12e2a 100%);
  background-image:      -o-linear-gradient(top, #d9534f 0%, #c12e2a 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#d9534f), to(#c12e2a));
  background-image:         linear-gradient(to bottom, #d9534f 0%, #c12e2a 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9534f', endColorstr='#ffc12e2a', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #b92c28;
}
.btn-danger:hover,
.btn-danger:focus {
  background-color: #c12e2a;
  background-position: 0 -15px;
}
.btn-danger:active,
.btn-danger.active {
  background-color: #c12e2a;
  border-color: #b92c28;
}
.btn-danger.disabled,
.btn-danger[disabled],
fieldset[disabled] .btn-danger,
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus,
.btn-danger.disabled:active,
.btn-danger[disabled]:active,
fieldset[disabled] .btn-danger:active,
.btn-danger.disabled.active,
.btn-danger[disabled].active,
fieldset[disabled] .btn-danger.active {
  background-color: #c12e2a;
  background-image: none;
}
.thumbnail,
.img-thumbnail {
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, .075);
          box-shadow: 0 1px 2px rgba(0, 0, 0, .075);
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  background-color: #e8e8e8;
  background-image: -webkit-linear-gradient(top, #f5f5f5 0%, #e8e8e8 100%);
  background-image:      -o-linear-gradient(top, #f5f5f5 0%, #e8e8e8 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f5f5f5), to(#e8e8e8));
  background-image:         linear-gradient(to bottom, #f5f5f5 0%, #e8e8e8 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff5f5f5', endColorstr='#ffe8e8e8', GradientType=0);
  background-repeat: repeat-x;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  background-color: #2e6da4;
  background-image: -webkit-linear-gradient(top, #337ab7 0%, #2e6da4 100%);
  background-image:      -o-linear-gradient(top, #337ab7 0%, #2e6da4 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#337ab7), to(#2e6da4));
  background-image:         linear-gradient(to bottom, #337ab7 0%, #2e6da4 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff337ab7', endColorstr='#ff2e6da4', GradientType=0);
  background-repeat: repeat-x;
}
.navbar-default {
  background-image: -webkit-linear-gradient(top, #fff 0%, #f8f8f8 100%);
  background-image:      -o-linear-gradient(top, #fff 0%, #f8f8f8 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#fff), to(#f8f8f8));
  background-image:         linear-gradient(to bottom, #fff 0%, #f8f8f8 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#fff8f8f8', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-radius: 4px;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .15), 0 1px 5px rgba(0, 0, 0, .075);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, .15), 0 1px 5px rgba(0, 0, 0, .075);
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .active > a {
  background-image: -webkit-linear-gradient(top, #dbdbdb 0%, #e2e2e2 100%);
  background-image:      -o-linear-gradient(top, #dbdbdb 0%, #e2e2e2 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#dbdbdb), to(#e2e2e2));
  background-image:         linear-gradient(to bottom, #dbdbdb 0%, #e2e2e2 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffdbdbdb', endColorstr='#ffe2e2e2', GradientType=0);
  background-repeat: repeat-x;
  -webkit-box-shadow: inset 0 3px 9px rgba(0, 0, 0, .075);
          box-shadow: inset 0 3px 9px rgba(0, 0, 0, .075);
}
.navbar-brand,
.navbar-nav > li > a {
  text-shadow: 0 1px 0 rgba(255, 255, 255, .25);
}
.navbar-inverse {
  background-image: -webkit-linear-gradient(top, #3c3c3c 0%, #222 100%);
  background-image:      -o-linear-gradient(top, #3c3c3c 0%, #222 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#3c3c3c), to(#222));
  background-image:         linear-gradient(to bottom, #3c3c3c 0%, #222 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff3c3c3c', endColorstr='#ff222222', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-radius: 4px;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .active > a {
  background-image: -webkit-linear-gradient(top, #080808 0%, #0f0f0f 100%);
  background-image:      -o-linear-gradient(top, #080808 0%, #0f0f0f 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#080808), to(#0f0f0f));
  background-image:         linear-gradient(to bottom, #080808 0%, #0f0f0f 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff080808', endColorstr='#ff0f0f0f', GradientType=0);
  background-repeat: repeat-x;
  -webkit-box-shadow: inset 0 3px 9px rgba(0, 0, 0, .25);
          box-shadow: inset 0 3px 9px rgba(0, 0, 0, .25);
}
.navbar-inverse .navbar-brand,
.navbar-inverse .navbar-nav > li > a {
  text-shadow: 0 -1px 0 rgba(0, 0, 0, .25);
}
.navbar-static-top,
.navbar-fixed-top,
.navbar-fixed-bottom {
  border-radius: 0;
}
@media (max-width: 767px) {
  .navbar .navbar-nav .open .dropdown-menu > .active > a,
  .navbar .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-image: -webkit-linear-gradient(top, #337ab7 0%, #2e6da4 100%);
    background-image:      -o-linear-gradient(top, #337ab7 0%, #2e6da4 100%);
    background-image: -webkit-gradient(linear, left top, left bottom, from(#337ab7), to(#2e6da4));
    background-image:         linear-gradient(to bottom, #337ab7 0%, #2e6da4 100%);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff337ab7', endColorstr='#ff2e6da4', GradientType=0);
    background-repeat: repeat-x;
  }
}
.alert {
  text-shadow: 0 1px 0 rgba(255, 255, 255, .2);
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .25), 0 1px 2px rgba(0, 0, 0, .05);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, .25), 0 1px 2px rgba(0, 0, 0, .05);
}
.alert-success {
  background-image: -webkit-linear-gradient(top, #dff0d8 0%, #c8e5bc 100%);
  background-image:      -o-linear-gradient(top, #dff0d8 0%, #c8e5bc 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#dff0d8), to(#c8e5bc));
  background-image:         linear-gradient(to bottom, #dff0d8 0%, #c8e5bc 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffdff0d8', endColorstr='#ffc8e5bc', GradientType=0);
  background-repeat: repeat-x;
  border-color: #b2dba1;
}
.alert-info {
  background-image: -webkit-linear-gradient(top, #d9edf7 0%, #b9def0 100%);
  background-image:      -o-linear-gradient(top, #d9edf7 0%, #b9def0 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#d9edf7), to(#b9def0));
  background-image:         linear-gradient(to bottom, #d9edf7 0%, #b9def0 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9edf7', endColorstr='#ffb9def0', GradientType=0);
  background-repeat: repeat-x;
  border-color: #9acfea;
}
.alert-warning {
  background-image: -webkit-linear-gradient(top, #fcf8e3 0%, #f8efc0 100%);
  background-image:      -o-linear-gradient(top, #fcf8e3 0%, #f8efc0 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#fcf8e3), to(#f8efc0));
  background-image:         linear-gradient(to bottom, #fcf8e3 0%, #f8efc0 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffcf8e3', endColorstr='#fff8efc0', GradientType=0);
  background-repeat: repeat-x;
  border-color: #f5e79e;
}
.alert-danger {
  background-image: -webkit-linear-gradient(top, #f2dede 0%, #e7c3c3 100%);
  background-image:      -o-linear-gradient(top, #f2dede 0%, #e7c3c3 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f2dede), to(#e7c3c3));
  background-image:         linear-gradient(to bottom, #f2dede 0%, #e7c3c3 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff2dede', endColorstr='#ffe7c3c3', GradientType=0);
  background-repeat: repeat-x;
  border-color: #dca7a7;
}
.progress {
  background-image: -webkit-linear-gradient(top, #ebebeb 0%, #f5f5f5 100%);
  background-image:      -o-linear-gradient(top, #ebebeb 0%, #f5f5f5 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#ebebeb), to(#f5f5f5));
  background-image:         linear-gradient(to bottom, #ebebeb 0%, #f5f5f5 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffebebeb', endColorstr='#fff5f5f5', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar {
  background-image: -webkit-linear-gradient(top, #337ab7 0%, #286090 100%);
  background-image:      -o-linear-gradient(top, #337ab7 0%, #286090 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#337ab7), to(#286090));
  background-image:         linear-gradient(to bottom, #337ab7 0%, #286090 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff337ab7', endColorstr='#ff286090', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-success {
  background-image: -webkit-linear-gradient(top, #5cb85c 0%, #449d44 100%);
  background-image:      -o-linear-gradient(top, #5cb85c 0%, #449d44 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#5cb85c), to(#449d44));
  background-image:         linear-gradient(to bottom, #5cb85c 0%, #449d44 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5cb85c', endColorstr='#ff449d44', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-info {
  background-image: -webkit-linear-gradient(top, #5bc0de 0%, #31b0d5 100%);
  background-image:      -o-linear-gradient(top, #5bc0de 0%, #31b0d5 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#5bc0de), to(#31b0d5));
  background-image:         linear-gradient(to bottom, #5bc0de 0%, #31b0d5 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff31b0d5', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-warning {
  background-image: -webkit-linear-gradient(top, #f0ad4e 0%, #ec971f 100%);
  background-image:      -o-linear-gradient(top, #f0ad4e 0%, #ec971f 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f0ad4e), to(#ec971f));
  background-image:         linear-gradient(to bottom, #f0ad4e 0%, #ec971f 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff0ad4e', endColorstr='#ffec971f', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-danger {
  background-image: -webkit-linear-gradient(top, #d9534f 0%, #c9302c 100%);
  background-image:      -o-linear-gradient(top, #d9534f 0%, #c9302c 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#d9534f), to(#c9302c));
  background-image:         linear-gradient(to bottom, #d9534f 0%, #c9302c 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9534f', endColorstr='#ffc9302c', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image:      -o-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image:         linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
}
.list-group {
  border-radius: 4px;
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, .075);
          box-shadow: 0 1px 2px rgba(0, 0, 0, .075);
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  text-shadow: 0 -1px 0 #286090;
  background-image: -webkit-linear-gradient(top, #337ab7 0%, #2b669a 100%);
  background-image:      -o-linear-gradient(top, #337ab7 0%, #2b669a 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#337ab7), to(#2b669a));
  background-image:         linear-gradient(to bottom, #337ab7 0%, #2b669a 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff337ab7', endColorstr='#ff2b669a', GradientType=0);
  background-repeat: repeat-x;
  border-color: #2b669a;
}
.list-group-item.active .badge,
.list-group-item.active:hover .badge,
.list-group-item.active:focus .badge {
  text-shadow: none;
}
.panel {
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, .05);
          box-shadow: 0 1px 2px rgba(0, 0, 0, .05);
}
.panel-default > .panel-heading {
  background-image: -webkit-linear-gradient(top, #f5f5f5 0%, #e8e8e8 100%);
  background-image:      -o-linear-gradient(top, #f5f5f5 0%, #e8e8e8 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f5f5f5), to(#e8e8e8));
  background-image:         linear-gradient(to bottom, #f5f5f5 0%, #e8e8e8 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff5f5f5', endColorstr='#ffe8e8e8', GradientType=0);
  background-repeat: repeat-x;
}
.panel-primary > .panel-heading {
  background-image: -webkit-linear-gradient(top, #337ab7 0%, #2e6da4 100%);
  background-image:      -o-linear-gradient(top, #337ab7 0%, #2e6da4 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#337ab7), to(#2e6da4));
  background-image:         linear-gradient(to bottom, #337ab7 0%, #2e6da4 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff337ab7', endColorstr='#ff2e6da4', GradientType=0);
  background-repeat: repeat-x;
}
.panel-success > .panel-heading {
  background-image: -webkit-linear-gradient(top, #dff0d8 0%, #d0e9c6 100%);
  background-image:      -o-linear-gradient(top, #dff0d8 0%, #d0e9c6 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#dff0d8), to(#d0e9c6));
  background-image:         linear-gradient(to bottom, #dff0d8 0%, #d0e9c6 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffdff0d8', endColorstr='#ffd0e9c6', GradientType=0);
  background-repeat: repeat-x;
}
.panel-info > .panel-heading {
  background-image: -webkit-linear-gradient(top, #d9edf7 0%, #c4e3f3 100%);
  background-image:      -o-linear-gradient(top, #d9edf7 0%, #c4e3f3 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#d9edf7), to(#c4e3f3));
  background-image:         linear-gradient(to bottom, #d9edf7 0%, #c4e3f3 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9edf7', endColorstr='#ffc4e3f3', GradientType=0);
  background-repeat: repeat-x;
}
.panel-warning > .panel-heading {
  background-image: -webkit-linear-gradient(top, #fcf8e3 0%, #faf2cc 100%);
  background-image:      -o-linear-gradient(top, #fcf8e3 0%, #faf2cc 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#fcf8e3), to(#faf2cc));
  background-image:         linear-gradient(to bottom, #fcf8e3 0%, #faf2cc 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffcf8e3', endColorstr='#fffaf2cc', GradientType=0);
  background-repeat: repeat-x;
}
.panel-danger > .panel-heading {
  background-image: -webkit-linear-gradient(top, #f2dede 0%, #ebcccc 100%);
  background-image:      -o-linear-gradient(top, #f2dede 0%, #ebcccc 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f2dede), to(#ebcccc));
  background-image:         linear-gradient(to bottom, #f2dede 0%, #ebcccc 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff2dede', endColorstr='#ffebcccc', GradientType=0);
  background-repeat: repeat-x;
}
.well {
  background-image: -webkit-linear-gradient(top, #e8e8e8 0%, #f5f5f5 100%);
  background-image:      -o-linear-gradient(top, #e8e8e8 0%, #f5f5f5 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#e8e8e8), to(#f5f5f5));
  background-image:         linear-gradient(to bottom, #e8e8e8 0%, #f5f5f5 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffe8e8e8', endColorstr='#fff5f5f5', GradientType=0);
  background-repeat: repeat-x;
  border-color: #dcdcdc;
  -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, .05), 0 1px 0 rgba(255, 255, 255, .1);
          box-shadow: inset 0 1px 3px rgba(0, 0, 0, .05), 0 1px 0 rgba(255, 255, 255, .1);
}
</style><style type="text/css">@charset "UTF-8";
.student-workspace.scoped-bootstrap:not(#modals-root) {
  padding: 0px;
  margin: 0;
  position: absolute;
  left: 0%;
  right: 0%;
  top: 0%;
  bottom: 0%;
  overflow: hidden;
  line-height: normal;
  font-family: "Open Sans", sans-serif; }
  .student-workspace.scoped-bootstrap:not(#modals-root) .theme_light {
    background-color: #ddd; }
  .student-workspace.scoped-bootstrap:not(#modals-root) .theme_dark {
    background-color: #657b83; }
  .student-workspace.scoped-bootstrap:not(#modals-root).inline {
    box-shadow: inset 0 -1px 0 0 #0F1820; }
  .student-workspace.scoped-bootstrap:not(#modals-root).attached {
    border-radius: 6px 6px 0 0; }

canvas {
  -webkit-touch-callout: none;
  outline: none;
  -webkit-tap-highlight-color: rgba(255, 255, 255, 0); }

form {
  margin: 0px; }
  form input {
    line-height: normal; }

.loading_backdrop {
  position: absolute;
  width: 100%;
  height: 100%;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  color: #999; }
  .theme_light .loading_backdrop {
    background-color: white; }
  .theme_dark .loading_backdrop {
    background-color: #657b83; }

.unselectable {
  -moz-user-select: -moz-none;
  -khtml-user-select: none;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none; }

.hidden-xs-inline {
  display: inline-block !important; }
  @media (max-width: 767px) {
    .hidden-xs-inline {
      display: none !important; } }

.student-workspace.scoped-bootstrap .btn {
  font-size: 12px;
  font-weight: 600;
  line-height: 24px;
  letter-spacing: 2px;
  white-space: normal;
  background-image: none;
  color: white;
  border: none; }
  .student-workspace.scoped-bootstrap .btn.btn-primary {
    text-shadow: none;
    background-color: #02B3E4;
    box-shadow: 12px 15px 20px 0 rgba(0, 0, 0, 0.1);
    transition: 0.2s box-shadow ease-in-out, 0.2s background-color ease-in-out, 0.2s border-color ease-in-out; }
    .student-workspace.scoped-bootstrap .btn.btn-primary:hover, .student-workspace.scoped-bootstrap .btn.btn-primary:focus, .student-workspace.scoped-bootstrap .btn.btn-primary:active {
      background-color: #148BB1;
      box-shadow: 2px 4px 8px 0 rgba(0, 0, 0, 0.1); }
  .student-workspace.scoped-bootstrap .btn.btn-default {
    text-shadow: none;
    background-color: #808080; }
    .student-workspace.scoped-bootstrap .btn.btn-default:hover, .student-workspace.scoped-bootstrap .btn.btn-default:focus, .student-workspace.scoped-bootstrap .btn.btn-default:active {
      background-color: #737373;
      color: white; }

.theme_dark .tooltip .tooltip-arrow {
  border-bottom-color: #252525; }

.theme_dark .tooltip .tooltip-inner {
  background-color: #252525; }

.tooltip-subtitle {
  font-size: 85%;
  color: #bbb;
  text-transform: uppercase; }

.student-workspace.scoped-bootstrap .navbar {
  min-height: 0;
  border: none; }

.student-workspace.scoped-bootstrap .navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  text-shadow: none; }

.student-workspace.scoped-bootstrap .navbar-brand,
.student-workspace.scoped-bootstrap .navbar-nav > li > a {
  text-shadow: none; }

.student-workspace.scoped-bootstrap .dropdown-submenu {
  position: relative; }
  .student-workspace.scoped-bootstrap .dropdown-submenu > .dropdown-menu {
    top: 0;
    left: 100%;
    margin-top: -6px;
    margin-left: -1px;
    -webkit-border-radius: 0 6px 6px 6px;
    -moz-border-radius: 0 6px 6px 6px;
    border-radius: 0 6px 6px 6px; }
  .student-workspace.scoped-bootstrap .dropdown-submenu > a:after {
    display: block;
    content: " ";
    float: right;
    width: 0;
    height: 0;
    border-color: transparent;
    border-style: solid;
    border-width: 5px 0 5px 5px;
    margin-top: 5px;
    margin-right: -10px; }

.student-workspace.scoped-bootstrap .theme_light .dropdown-submenu > a:after {
  border-left-color: #555555; }

.student-workspace.scoped-bootstrap .theme_dark .dropdown-submenu > a:after {
  border-left-color: #aaaaaa; }

.student-workspace.scoped-bootstrap .dropdown-menu {
  margin: 0px;
  min-width: 220px; }

.student-workspace.scoped-bootstrap .theme_light .dropdown-menu {
  background-color: #fff; }
  .student-workspace.scoped-bootstrap .theme_light .dropdown-menu a {
    color: #000; }
    .student-workspace.scoped-bootstrap .theme_light .dropdown-menu a:hover, .student-workspace.scoped-bootstrap .theme_light .dropdown-menu a:focus {
      background-image: none;
      background-color: #eee; }

.student-workspace.scoped-bootstrap .theme_dark .dropdown-menu {
  background-color: #073642; }
  .student-workspace.scoped-bootstrap .theme_dark .dropdown-menu a {
    color: #93a1a1; }
    .student-workspace.scoped-bootstrap .theme_dark .dropdown-menu a:hover, .student-workspace.scoped-bootstrap .theme_dark .dropdown-menu a:focus {
      background-color: #586e75;
      color: #fdf6e3;
      background-image: none; }
  .student-workspace.scoped-bootstrap .theme_dark .dropdown-menu li.divider {
    background-color: #a0a0a0; }

.student-workspace.scoped-bootstrap .navbar-default {
  -webkit-box-shadow: none !important;
  box-shadow: none !important; }

.student-workspace.scoped-bootstrap .navbar-static-top {
  margin-bottom: 0; }

.student-workspace.scoped-bootstrap .navbar {
  margin-bottom: 0;
  border-radius: 0px; }

.student-workspace.scoped-bootstrap .nav-logged-out {
  color: #00f;
  background: 0 !important;
  background-image: none !important;
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
  background: none !important;
  padding-top: 10px;
  padding-bottom: 10px; }

.student-workspace.scoped-bootstrap .nav-logged-in {
  margin-bottom: 0 !important;
  margin-top: 0 !important;
  padding-bottom: 0 !important;
  min-height: 10px !important;
  font-size: 13px !important;
  font-style: normal !important;
  font-variant: normal !important;
  font-weight: bold !important; }

.student-workspace.scoped-bootstrap .nav-logged-in a {
  padding: 10px 0 10px 15px !important;
  color: #364655 !important; }

.student-workspace.scoped-bootstrap .nav-logged-out .link {
  padding: 10px 0 10px 10px !important; }

.student-workspace.scoped-bootstrap .nav-logged-out .btn {
  margin-top: 5px;
  margin-bottom: 5px;
  padding: 5px 10px 5px 10px !important;
  margin-left: 10px; }

.student-workspace.scoped-bootstrap .navbar-nav > li > .dropdown-menu {
  border-top-right-radius: 4px;
  border-top-left-radius: 4px; }

.student-workspace.scoped-bootstrap .navbar-nav > li > .dropdown-menu.dropdown-popover {
  margin: 0;
  padding: 0;
  min-height: 80px;
  overflow-y: scroll; }

.student-workspace.scoped-bootstrap .dropdown-loading-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  font-size: 20px;
  margin: -10px;
  color: #999;
  z-index: -1; }

.student-workspace.scoped-bootstrap iframe.dropdown-iframe {
  display: block;
  border-radius: 4px;
  border: none;
  outline: none;
  box-shadow: none;
  -moz-box-shadow: none;
  -webkit-box-shadow: none; }

.student-workspace.scoped-bootstrap .featurette {
  padding: 40px;
  margin-bottom: 0; }

.student-workspace.scoped-bootstrap .featurette:nth-of-type(even) {
  background: #e7e7e7 !important; }

.student-workspace.scoped-bootstrap .featurette:nth-of-type(odd) {
  background: white !important; }

.student-workspace.scoped-bootstrap hr.before_footer {
  margin: 40px 0; }

.student-workspace.scoped-bootstrap .index-page #sign-up {
  display: none; }

.student-workspace.scoped-bootstrap .nav-logged-out .btn-success {
  color: white !important; }

.student-workspace.scoped-bootstrap .navbar-form {
  margin-top: 5px;
  margin-bottom: 5px; }

.student-workspace.scoped-bootstrap .nav span.glyphicon {
  padding-bottom: 15px;
  margin-bottom: -15px; }

#brand {
  color: #000;
  padding-top: 5px !important;
  padding-bottom: 5px !important;
  padding-right: 15px !important;
  border-right: 1px solid #e7e7e7; }

.index_page .jumbotron {
  background: #000;
  color: #fff;
  background: -webkit-linear-gradient(right, gray, black);
  background: -moz-linear-gradient(right, gray, black);
  background: -o-linear-gradient(right, gray, black);
  background: -ms-linear-gradient(right, gray, black);
  background: linear-gradient(to left, gray, black); }

.footer {
  text-align: center;
  padding: 30px 0;
  margin-top: 70px;
  border-top: 1px solid #e5e5e5;
  background-color: whitesmoke; }

.footer p {
  margin-bottom: 0;
  color: #777777; }

.footer-links {
  margin: 10px 0; }

.footer-links li {
  display: inline;
  padding: 0 2px; }

.footer-links li:first-child {
  padding-left: 0; }

.thumbnail {
  padding: 10px; }

.no_login_buttons .navbar-form {
  display: none; }

.no_login_buttons #features {
  padding-right: 0px; }

.student-workspace.scoped-bootstrap .button-navbar {
  font-size: 13px;
  width: 100%;
  margin-top: 0; }
  .student-workspace.scoped-bootstrap .button-navbar i {
    vertical-align: text-bottom; }
  .student-workspace.scoped-bootstrap .button-navbar > ul {
    text-align: center; }
    .student-workspace.scoped-bootstrap .button-navbar > ul > li {
      display: inline-block;
      line-height: 25px; }
      .student-workspace.scoped-bootstrap .button-navbar > ul > li.disabled {
        pointer-events: none; }
      .student-workspace.scoped-bootstrap .button-navbar > ul > li > a {
        padding: 5px 8px;
        background: none !important; }

.theme_light .button-navbar {
  background-color: #FBFBFA;
  border-bottom: 1px solid #f0f0f0; }
  .theme_light .button-navbar, .theme_light .button-navbar a, .theme_light .button-navbar li {
    color: black; }
  .theme_light .button-navbar li:hover {
    background-color: #eee; }
  .theme_light .button-navbar li.active {
    background-color: #e8e8e8; }

.theme_dark .button-navbar {
  background-color: #24323E; }
  .theme_dark .button-navbar, .theme_dark .button-navbar a, .theme_dark .button-navbar li {
    color: #93a1a1; }
  .theme_dark .button-navbar li > a:hover {
    background-color: #586e75; }

.student-workspace.scoped-bootstrap {
  font-family: "Open Sans", sans-serif; }
  .student-workspace.scoped-bootstrap .modal-dialog {
    margin: 50px auto; }
    @media (max-width: 767px) {
      .student-workspace.scoped-bootstrap .modal-dialog {
        width: auto;
        margin: 40px 40px; } }
  .student-workspace.scoped-bootstrap .modal-content {
    overflow: hidden;
    border: none; }
  .student-workspace.scoped-bootstrap .modal-close {
    position: absolute;
    right: -30px;
    top: -42px;
    color: #337AB7;
    font-size: xx-large;
    font-weight: 300;
    line-height: 1;
    opacity: 1;
    cursor: pointer;
    text-shadow: none; }
  .student-workspace.scoped-bootstrap .theme_dark .modal-header {
    background-color: #073642;
    border-bottom: 1px solid #444444 !important;
    color: #888888; }
  .student-workspace.scoped-bootstrap .theme_dark .modal-body {
    color: #93a1a1;
    background-color: #073642; }
  .student-workspace.scoped-bootstrap .theme_light .modal-body {
    background-color: white;
    color: #525C65; }

#text_shown {
  width: 100%;
  border: 1px;
  padding: 10px;
  margin: 10px; }
  .theme_light #text_shown {
    background-color: #eeeeee; }
  .theme_dark #text_shown {
    background-color: #111111; }

#confirm_modal .modal-dialog {
  width: 400px; }
  #confirm_modal .modal-dialog p {
    margin: 5px 0 15px; }

.student-workspace.scoped-bootstrap .context-menu-list {
  margin: 0;
  padding: 0;
  min-width: 120px;
  max-width: 250px;
  display: inline-block;
  position: fixed;
  list-style-type: none;
  overflow: hidden;
  border-radius: 4px;
  background: white;
  transform: translate(5px); }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-item {
  padding: 6px 9px;
  position: relative;
  -webkit-user-select: none;
  -moz-user-select: -moz-none;
  -ms-user-select: none;
  user-select: none;
  cursor: default;
  line-height: 24px;
  font-size: 14px;
  font-weight: 600; }

.context-menu-list .context-menu-item {
  color: #02B3E4; }
  .context-menu-list .context-menu-item:hover {
    background-color: #F4F6F8; }
  .context-menu-list .context-menu-item.disabled, .context-menu-list .context-menu-item.disabled:hover {
    color: #eee; }

.context-menu-item.delete {
  color: #dc322f; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-item > label > input,
.student-workspace.scoped-bootstrap .context-menu-list .context-menu-item > label > textarea {
  -webkit-user-select: text;
  -moz-user-select: text;
  -ms-user-select: text;
  user-select: text; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-item > .context-menu-list {
  display: none;
  right: -5px;
  top: 5px; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-item:hover > .context-menu-list {
  display: block; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-separator {
  height: 1px;
  padding: 0px;
  margin: 3px 0px;
  background-color: lightgray; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-submenu:after {
  content: ">";
  color: #444;
  position: absolute;
  top: 5px;
  right: 3px;
  z-index: 1; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-input > label,
.student-workspace.scoped-bootstrap .context-menu-list .context-menu-input > label > input[type="text"],
.student-workspace.scoped-bootstrap .context-menu-list .context-menu-input > label > textarea,
.student-workspace.scoped-bootstrap .context-menu-list .context-menu-input > label > select {
  display: block;
  width: 100%;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  -ms-box-sizing: border-box;
  -o-box-sizing: border-box;
  box-sizing: border-box; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-input > label > * {
  vertical-align: top; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-input > label > input[type="checkbox"],
.student-workspace.scoped-bootstrap .context-menu-list .context-menu-input > label > input[type="radio"] {
  margin-left: -17px; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-input > label > span {
  margin-left: 5px; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-input > label > textarea {
  height: 100px; }

.student-workspace.scoped-bootstrap .context-menu-list .context-menu-accesskey {
  text-decoration: underline; }

.manager_pane {
  display: none; }

.student-workspace.scoped-bootstrap .panel {
  padding: 0px;
  position: absolute;
  width: auto;
  height: auto;
  margin: 0;
  border-radius: 0;
  overflow: hidden;
  color: #24323E;
  z-index: auto; }

.student-workspace.scoped-bootstrap .theme_light .panel {
  background-color: white;
  border: 1px solid #c8c8c8; }

.student-workspace.scoped-bootstrap .theme_dark .panel {
  background-color: #24323E;
  border: 1px solid #1C262F; }

.student-workspace.scoped-bootstrap .panel.active {
  border-color: #2aa198; }

.student-workspace.scoped-bootstrap .panel .empty_panel {
  text-align: center;
  color: #DBE2E8;
  line-height: 24px;
  font-size: 14px;
  font-family: "Open Sans", sans-serif; }
  .student-workspace.scoped-bootstrap .panel .empty_panel.shell_terminal {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center; }
  .student-workspace.scoped-bootstrap .panel .empty_panel .empty_icon {
    display: inline-block;
    height: 48px;
    width: 48px; }
    .student-workspace.scoped-bootstrap .panel .empty_panel .empty_icon.editor {
      background-image: url(/images/code-editor-empty-30225.svg); }
    .student-workspace.scoped-bootstrap .panel .empty_panel .empty_icon.terminal_shell {
      background-image: url(/images/shell-editor-empty-31400.svg); }
  .student-workspace.scoped-bootstrap .panel .empty_panel .empty_message {
    margin-top: -5px; }
  .student-workspace.scoped-bootstrap .panel .empty_panel .empty_newtab {
    font-size: 12px;
    font-weight: 600;
    line-height: 24px;
    letter-spacing: 2px;
    white-space: normal;
    text-decoration: none;
    color: #02B3E4;
    display: inline-block;
    padding-top: 24px; }
    .student-workspace.scoped-bootstrap .panel .empty_panel .empty_newtab:hover, .student-workspace.scoped-bootstrap .panel .empty_panel .empty_newtab:focus, .student-workspace.scoped-bootstrap .panel .empty_panel .empty_newtab:active {
      color: #148BB1; }

.student-workspace.scoped-bootstrap .panel_dock > a {
  cursor: pointer; }

.student-workspace.scoped-bootstrap .tab_bar {
  left: 0;
  width: auto;
  padding: 1px 0;
  z-index: 2;
  top: 0;
  right: 0;
  height: 40px;
  margin: 0; }

.student-workspace.scoped-bootstrap .theme_dark .tab_bar,
.student-workspace.scoped-bootstrap .theme_dark .tab_bar .info_pane {
  background-color: #1C262F;
  border-bottom: 1px solid #1C262F; }

.student-workspace.scoped-bootstrap .theme_light .tab_bar,
.student-workspace.scoped-bootstrap .theme_light .tab_bar .info_pane {
  background-color: #eee; }

.student-workspace.scoped-bootstrap .info_pane {
  z-index: 2;
  top: 0;
  right: 0;
  height: 40px;
  margin: 0;
  line-height: 40px;
  position: absolute; }

.student-workspace.scoped-bootstrap .theme_light .info_pane {
  color: #aaa;
  border-left: 1px solid #ccc; }

.student-workspace.scoped-bootstrap .theme_dark .info_pane {
  color: #888;
  border-left: 1px solid #555; }

.student-workspace.scoped-bootstrap .tab.term {
  width: 205px; }

.closetab {
  float: right;
  border-radius: 9px;
  width: 18px;
  height: 18px;
  line-height: 18px;
  font-size: 24px;
  margin: 10px 8px;
  text-align: center;
  color: #7D97AD; }
  .closetab:hover {
    color: #FFFFFF; }

.student-workspace.scoped-bootstrap .tab {
  float: left;
  font-size: 14px;
  font-weight: 400;
  margin: 0;
  cursor: default;
  height: 39px;
  line-height: 17px;
  overflow: hidden;
  position: relative;
  color: #7D97AD; }
  .student-workspace.scoped-bootstrap .tab.active {
    display: block;
    margin-bottom: -4px;
    border-right: 2px solid #1C262F;
    border-left: 2px solid #1C262F; }
  .student-workspace.scoped-bootstrap .tab:hover {
    background: #344655;
    color: #FFFFFF; }

.student-workspace.scoped-bootstrap .tab_title {
  margin: 8px 20px;
  line-height: 24px;
  display: inline-block; }

.theme_dark .tab.active {
  background-color: #24323E;
  color: #FFFFFF;
  border-color: #24323E; }

.student-workspace.scoped-bootstrap .tab.newtab {
  width: 48px;
  background-color: #1C262F;
  display: flex;
  align-items: center;
  justify-content: center; }
  .student-workspace.scoped-bootstrap .tab.newtab span {
    line-height: 16px;
    height: 21px;
    width: 19px;
    display: block;
    font-size: xx-large; }

.student-workspace.scoped-bootstrap .theme_dark .tab.newtab:hover {
  color: #FFFFFF;
  background: #586e75; }

.content_div {
  position: absolute;
  width: auto;
  height: auto;
  left: 0;
  top: 40px;
  right: 0;
  bottom: 0;
  overflow: hidden;
  white-space: nowrap;
  margin: 0;
  border: 0;
  font-family: "source-code-pro", monospace;
  font-size: 12px;
  font-style: normal;
  font-variant: normal;
  font-weight: normal;
  z-index: 1; }

.resize {
  position: absolute;
  display: block;
  opacity: 0;
  z-index: 9;
  color-profile: sRGB;
  border: 1px solid red;
  background: red; }

.resize_x {
  cursor: ew-resize;
  height: auto;
  right: auto; }

.resize_y {
  cursor: ns-resize;
  width: auto;
  bottom: auto; }

.cm-s-udacity {
  z-index: 1; }

#files_modal *:not(input.field) {
  -moz-user-select: -moz-none;
  -khtml-user-select: none;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none; }

#files_modal .modal-body {
  padding: 0; }

#files_modal #files_modal_name_select {
  box-shadow: 0 0 15px 0 rgba(46, 61, 73, 0.2);
  padding: 20px;
  width: 100%;
  display: flex;
  flex-direction: row; }
  #files_modal #files_modal_name_select .files-modal--input {
    flex-grow: 1;
    margin-right: 16px; }
  #files_modal #files_modal_name_select .files-modal--submit {
    flex-basis: 168px; }

#files_modal .modal-content {
  overflow: hidden; }

#files_modal td.file_dropdown {
  pointer-events: none;
  visibility: hidden; }

#files_modal .files-modal-table-container {
  padding: 10px 32px 0px;
  overflow-y: auto;
  height: 320px; }

#files_modal #react-file-list {
  table-layout: fixed; }

#files_modal #files_modal_display {
  margin-bottom: 20px;
  width: 100%;
  cursor: default; }
  #files_modal #files_modal_display th {
    font-family: "Open Sans", sans-serif;
    font-weight: 600;
    font-size: 12px;
    letter-spacing: 2px;
    color: #525C65;
    text-transform: uppercase; }
    .theme_light #files_modal #files_modal_display th {
      border-bottom: 1px solid #DBE2E8 !important; }
    .theme_dark #files_modal #files_modal_display th {
      border-bottom: 1px solid #444 !important; }
  #files_modal #files_modal_display td, #files_modal #files_modal_display th {
    border: 0 !important;
    white-space: nowrap; }
    #files_modal #files_modal_display td.file_name, #files_modal #files_modal_display th.file_name {
      padding-left: 12px;
      user-select: none;
      line-height: 18px; }
      #files_modal #files_modal_display td.file_name a, #files_modal #files_modal_display th.file_name a {
        display: inline-block; }
        .theme_dark #files_modal #files_modal_display td.file_name a,
        .theme_light #files_modal #files_modal_display td.file_name a, .theme_dark #files_modal #files_modal_display th.file_name a,
        .theme_light #files_modal #files_modal_display th.file_name a {
          color: inherit; }
        #files_modal #files_modal_display td.file_name a:hover, #files_modal #files_modal_display td.file_name a:focus, #files_modal #files_modal_display th.file_name a:hover, #files_modal #files_modal_display th.file_name a:focus {
          text-decoration: none; }
    #files_modal #files_modal_display td .file_name_text, #files_modal #files_modal_display th .file_name_text {
      margin: 0 8px 0 10px; }
    #files_modal #files_modal_display td.file_size, #files_modal #files_modal_display th.file_size {
      width: 20%; }
    #files_modal #files_modal_display td.file_mtime, #files_modal #files_modal_display th.file_mtime {
      width: 20%; }
  .theme_light #files_modal #files_modal_display tr.active td, .theme_light #files_modal #files_modal_display tr.active th, .theme_light #files_modal #files_modal_display tr.context-menu-active td, .theme_light #files_modal #files_modal_display tr.context-menu-active th {
    background-color: #FAFBFC; }
  .theme_dark #files_modal #files_modal_display tr.active td, .theme_dark #files_modal #files_modal_display tr.active th, .theme_dark #files_modal #files_modal_display tr.context-menu-active td, .theme_dark #files_modal #files_modal_display tr.context-menu-active th {
    background-color: #344655; }
  .theme_dark #files_modal #files_modal_display tr {
    color: #DBE2E8; }
  .theme_light #files_modal #files_modal_display tr {
    color: #525C65; }
  .theme_light #files_modal #files_modal_display tr td.active, .theme_light #files_modal #files_modal_display tr th.active {
    background-color: #bde3f7; }
  .theme_dark #files_modal #files_modal_display tr td.active, .theme_dark #files_modal #files_modal_display tr th.active {
    background-color: #014b72; }
  #files_modal #files_modal_display .nav {
    margin-bottom: 0px; }
  #files_modal #files_modal_display .navbar {
    box-shadow: 0 0 15px 0 rgba(46, 61, 73, 0.2);
    height: 60px;
    padding: 20px; }
  #files_modal #files_modal_display .modal--back-arrow {
    display: inline-block;
    margin-left: 32px;
    list-style: none;
    color: #02B3E4; }
  #files_modal #files_modal_display .breadcrumbs {
    list-style: none;
    font-size: 14px;
    line-height: 22px;
    margin: 0px;
    display: inline-block; }
    .theme_dark #files_modal #files_modal_display .breadcrumbs > li {
      color: #7D97AD;
      display: inline-block; }
      .theme_dark #files_modal #files_modal_display .breadcrumbs > li a {
        text-decoration: none;
        color: #7D97AD; }
      .theme_dark #files_modal #files_modal_display .breadcrumbs > li:last-child {
        color: #FFFFFF;
        font-weight: 600; }
    .theme_light #files_modal #files_modal_display .breadcrumbs > li {
      color: #525C65;
      opacity: 0.8;
      display: inline-block; }
      .theme_light #files_modal #files_modal_display .breadcrumbs > li a {
        text-decoration: none;
        color: #525C65; }
      .theme_light #files_modal #files_modal_display .breadcrumbs > li span {
        color: #525C65; }
      .theme_light #files_modal #files_modal_display .breadcrumbs > li:last-child {
        color: #525C65;
        opacity: 1;
        font-weight: 600; }
    #files_modal #files_modal_display .breadcrumbs .divider {
      padding: 0 3px;
      color: #7D97AD; }

#files_modal #modal_files .file_name {
  text-overflow: ellipsis;
  overflow: hidden; }

#files_modal #files_modal_submit {
  margin-left: 10px;
  height: 48px;
  width: 100%; }

#files_modal #files_modal_input {
  height: 48px;
  width: 100%;
  padding: 16px;
  line-height: 16px;
  box-shadow: 5px 5px 10px 0 rgba(0, 0, 0, 0.05); }

.files-panel {
  position: absolute;
  width: auto;
  overflow: hidden;
  top: 0%;
  right: 90%;
  bottom: 0%;
  left: 0%;
  font-size: 14px; }
  .files-panel #files_container_inner {
    height: 100%;
    display: flex;
    flex-direction: column;
    margin: 0 15px;
    cursor: default; }
    @media (max-width: 1040px) {
      .files-panel #files_container_inner {
        margin: 0 5px; } }
    .files-panel #files_container_inner #files_navbar {
      display: flex;
      border-bottom: 1px solid #0F1820; }
    .files-panel #files_container_inner #files_toolbar {
      display: flex;
      flex-direction: row;
      width: 100%;
      color: #DBE2E8; }
      .files-panel #files_container_inner #files_toolbar li, .files-panel #files_container_inner #files_toolbar a {
        color: inherit; }
      .files-panel #files_container_inner #files_toolbar span {
        font-size: medium; }
        @media (max-width: 1040px) {
          .files-panel #files_container_inner #files_toolbar span {
            font-size: small; } }
      .files-panel #files_container_inner #files_toolbar .navigate_up {
        margin-right: auto; }
    .files-panel #files_container_inner #myCrumbs {
      flex-grow: 0;
      flex-shrink: 0;
      margin: 10px 0; }
    .files-panel #files_container_inner .breadcrumbs {
      list-style: none;
      font-size: 14px;
      line-height: 22px;
      margin: 0px; }
      .theme_dark .files-panel #files_container_inner .breadcrumbs > li {
        color: #7D97AD;
        display: inline-block; }
        .theme_dark .files-panel #files_container_inner .breadcrumbs > li a {
          text-decoration: none;
          color: #7D97AD; }
        .theme_dark .files-panel #files_container_inner .breadcrumbs > li:last-child {
          color: #FFFFFF;
          font-weight: 600; }
      .theme_light .files-panel #files_container_inner .breadcrumbs > li {
        color: #525C65;
        opacity: 0.8;
        display: inline-block; }
        .theme_light .files-panel #files_container_inner .breadcrumbs > li a {
          text-decoration: none;
          color: #525C65; }
        .theme_light .files-panel #files_container_inner .breadcrumbs > li span {
          color: #525C65; }
        .theme_light .files-panel #files_container_inner .breadcrumbs > li:last-child {
          color: #525C65;
          opacity: 1;
          font-weight: 600; }
      .files-panel #files_container_inner .breadcrumbs .divider {
        padding: 0 3px;
        color: #7D97AD; }
    .files-panel #files_container_inner .files-table-wrapper {
      flex-grow: 1;
      overflow: auto;
      margin-right: -32px; }
      .files-panel #files_container_inner .files-table-wrapper .files-table {
        margin-bottom: 0px !important; }
    .files-panel #files_container_inner th {
      font-family: "Open Sans", sans-serif;
      font-weight: 600;
      font-size: 12px;
      letter-spacing: 2px;
      color: #525C65;
      text-transform: uppercase; }
      .theme_light .files-panel #files_container_inner th {
        border-bottom: 1px solid #DBE2E8 !important; }
      .theme_dark .files-panel #files_container_inner th {
        border-bottom: 1px solid #444 !important; }
    .files-panel #files_container_inner td, .files-panel #files_container_inner th {
      border: 0 !important;
      white-space: nowrap; }
      .files-panel #files_container_inner td.file_name, .files-panel #files_container_inner th.file_name {
        padding-left: 12px;
        user-select: none;
        line-height: 18px; }
        .files-panel #files_container_inner td.file_name a, .files-panel #files_container_inner th.file_name a {
          display: inline-block; }
          .theme_dark .files-panel #files_container_inner td.file_name a,
          .theme_light .files-panel #files_container_inner td.file_name a, .theme_dark .files-panel #files_container_inner th.file_name a,
          .theme_light .files-panel #files_container_inner th.file_name a {
            color: inherit; }
          .files-panel #files_container_inner td.file_name a:hover, .files-panel #files_container_inner td.file_name a:focus, .files-panel #files_container_inner th.file_name a:hover, .files-panel #files_container_inner th.file_name a:focus {
            text-decoration: none; }
      .files-panel #files_container_inner td .file_name_text, .files-panel #files_container_inner th .file_name_text {
        margin: 0 8px 0 10px; }
      .files-panel #files_container_inner td.file_size, .files-panel #files_container_inner th.file_size {
        width: 20%; }
      .files-panel #files_container_inner td.file_mtime, .files-panel #files_container_inner th.file_mtime {
        width: 20%; }
    .theme_light .files-panel #files_container_inner tr.active td, .theme_light .files-panel #files_container_inner tr.active th, .theme_light .files-panel #files_container_inner tr.context-menu-active td, .theme_light .files-panel #files_container_inner tr.context-menu-active th {
      background-color: #FAFBFC; }
    .theme_dark .files-panel #files_container_inner tr.active td, .theme_dark .files-panel #files_container_inner tr.active th, .theme_dark .files-panel #files_container_inner tr.context-menu-active td, .theme_dark .files-panel #files_container_inner tr.context-menu-active th {
      background-color: #344655; }
    .theme_dark .files-panel #files_container_inner tr {
      color: #DBE2E8; }
    .theme_light .files-panel #files_container_inner tr {
      color: #525C65; }
    .theme_light .files-panel #files_container_inner tr td.active, .theme_light .files-panel #files_container_inner tr th.active {
      background-color: #bde3f7; }
    .theme_dark .files-panel #files_container_inner tr td.active, .theme_dark .files-panel #files_container_inner tr th.active {
      background-color: #014b72; }
    .files-panel #files_container_inner tbody.files_list {
      width: 100%;
      bottom: 0;
      left: 0;
      right: 0;
      margin: 0;
      padding: 0; }

#uploader {
  bottom: 0;
  left: 0;
  right: 0; }
  .theme_light #uploader {
    border-top: 1px solid #e5e5e5;
    background: #fbfbfa; }
  .theme_dark #uploader {
    border-top: 1px solid #1C262F;
    background: #24323E; }
  #uploader p {
    color: #7D97AD; }
  #uploader a.btn {
    font-size: 12px;
    line-height: 24px;
    letter-spacing: 2px;
    white-space: normal;
    font-family: "Open Sans", sans-serif; }
    @media (max-width: 1040px) {
      #uploader a.btn {
        font-size: 10px;
        line-height: 14px; } }

#upload_alerts {
  margin-bottom: 10px; }
  #upload_alerts .alert {
    position: relative;
    font-size: 90%;
    padding: 8px 10px 6px;
    margin: 10px 10px 0; }
    #upload_alerts .alert.alert-dismissable .close {
      position: absolute;
      top: 5px;
      right: 5px; }
    #upload_alerts .alert strong {
      display: inline-block;
      margin-bottom: -3px;
      max-width: 100%;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden; }

#upload_list {
  position: relative; }
  #upload_list > * {
    padding: 10px; }
    .theme_light #upload_list > * {
      border-top: 1px solid #e5e5e5; }
    .theme_dark #upload_list > * {
      border-top: 1px solid #444; }
  #upload_list .actions {
    display: inline-block;
    text-overflow: ellipsis;
    overflow: hidden;
    max-width: 100%; }
    .theme_light #upload_list .actions, .theme_light #upload_list .actions a {
      color: #444; }
    .theme_dark #upload_list .actions, .theme_dark #upload_list .actions a {
      color: #839496; }
    .theme_light #upload_list .actions .filename {
      color: black; }
    .theme_dark #upload_list .actions .filename {
      color: #eee; }
    #upload_list .actions a {
      font-size: 85%; }
  #upload_list .progress {
    height: 10px;
    margin: 5px 0; }

.CodeMirror {
  height: calc(100% - 58px);
  overflow: visible; }

.editor {
  height: calc(100% - 50px);
  display: flex;
  align-items: center;
  justify-content: center; }

.editor-loading {
  user-select: none;
  pointer-events: none;
  opacity: 0.5;
  background-color: grey;
  height: calc(100% - 30px);
  width: 100%;
  position: absolute;
  z-index: 5;
  text-align: center; }

.editor-loading.hidden {
  display: none; }

.editor-remote-selection-background-0 {
  background-color: #b58900; }

.editor-remote-selection-background-1 {
  background-color: #268bd2; }

.editor-remote-selection-background-2 {
  background-color: #cb4b16; }

.editor-remote-selection-background-3 {
  background-color: #dc322f; }

.editor-remote-selection-background-4 {
  background-color: #6c71c4; }

.editor-remote-selection-background-5 {
  background-color: #859900; }

.editor-tabs-wrapper .editor-tabs {
  width: 100%; }

.editor-tabs-wrapper .overflow-tab {
  display: none; }

.editor-tabs-wrapper.hasOverflow .editor-tabs {
  width: calc(100% - 20px); }

.editor-tabs-wrapper.hasOverflow .overflow-tab {
  display: block; }

.editor-tabs-wrapper .editor-tabs {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap; }
  .editor-tabs-wrapper .editor-tabs .tab {
    flex-basis: 50px;
    flex-grow: 1;
    max-width: 200px; }
    .editor-tabs-wrapper .editor-tabs .tab:first-child {
      border-left: 0px; }
    .editor-tabs-wrapper .editor-tabs .tab:last-child {
      border-right: 0px; }

.editor_tab {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap; }
  .editor_tab .editor_tab_text {
    margin: 8px 20px;
    line-height: 24px;
    display: inline-block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    flex-grow: 1; }
  .editor_tab .editor_tab_members {
    flex-basis: 10px; }
  .editor_tab .closetab {
    flex-basis: 20px; }

.editor_tab_members {
  display: none; }

.overflow-tab {
  position: absolute;
  top: 0;
  right: 0;
  width: 20px;
  display: inline-block;
  height: 30px;
  vertical-align: top;
  background-color: #a9a9a9; }
  .overflow-tab:before {
    content: "\F054";
    font-family: "FontAwesome";
    font-size: 12px;
    width: 20px;
    display: inline-block;
    text-align: center;
    line-height: 30px;
    color: white; }

.overflow-tab.active:before {
  content: "\F078"; }

.overflow-dropdown {
  position: absolute;
  right: 0px;
  background-color: white;
  z-index: 10001;
  list-style-type: none;
  padding-left: 0;
  width: 200px;
  box-shadow: 0 2px 6px 0 rgba(46, 60, 73, 0.2); }
  .overflow-dropdown li {
    padding: 5px 10px; }
    .overflow-dropdown li.active, .overflow-dropdown li:hover {
      background-color: #2aa198;
      color: white; }

#browser_container .html_button {
  position: absolute;
  padding: 8px;
  height: 32px;
  width: 29px;
  cursor: pointer;
  z-index: 1; }
  .theme_light #browser_container .html_button {
    color: black;
    background: #fbfbfa;
    border: 1px solid #dedede;
    border-top: none;
    border-left: none; }
    .theme_light #browser_container .html_button:hover, .theme_light #browser_container .html_button:focus {
      background: #eee; }
  .theme_dark #browser_container .html_button {
    color: #93a1a1;
    background: #24323E;
    border: 1px solid #586e75;
    border-top: none;
    border-left: none; }
    .theme_dark #browser_container .html_button:hover, .theme_dark #browser_container .html_button:focus {
      background: #839496;
      color: #24323E; }

#browser_container #html_form_container {
  position: relative;
  padding-left: 58px; }

#browser_container #html_url_input {
  width: 100%;
  height: 32px;
  padding-left: 7px;
  outline: none;
  border: none; }
  .theme_light #browser_container #html_url_input {
    border-bottom: 1px solid #dddddd; }
  .theme_dark #browser_container #html_url_input {
    border-bottom: 1px solid #586e75;
    background: #073642;
    color: #839496; }

#browser_container .html_frame {
  box-shadow: none;
  border: none;
  outline: none;
  width: 100%;
  height: 100%; }

#browser_container #html_content_div {
  top: 56px; }
  .theme_light #browser_container #html_content_div {
    background: white; }
  .theme_dark #browser_container #html_content_div {
    background: #24323E; }

.hotkeys-div {
  text-align: center; }

.hotkeys-config {
  background-color: #eee;
  border: 1px solid #ddd;
  line-height: 1.4;
  resize: none;
  width: 100%;
  overflow-y: scroll; }
  @media (min-height: 600px) {
    .hotkeys-config {
      max-height: 457px; } }
  @media (min-height: 800px) {
    .hotkeys-config {
      max-height: 557px; } }
  @media (min-height: 1000px) {
    .hotkeys-config {
      max-height: 757px; } }

.binding-input {
  width: 92%;
  display: inline-block;
  border-left: none;
  border-right: 1px solid #f0f0f0;
  border-top: none;
  text-align: center;
  border-bottom: none; }

.empty {
  width: 100%; }

.hotkey-delete {
  width: 8%;
  height: 19px;
  position: relative; }

.manager-div {
  text-align: left;
  background-color: #F5F5F5;
  padding: 3px; }

.hotkey-div {
  border-top: 2px solid #f0f0f0; }

.command-container {
  display: inline-block;
  width: 50%;
  vertical-align: top;
  margin-top: 2px; }

.command-div {
  width: 92%;
  display: inline-block; }

.add-div {
  width: 8%;
  height: 19px;
  position: relative; }

.bindings-div {
  width: 50%;
  text-align: center;
  display: inline-block;
  margin-right: 0px;
  margin-left: auto;
  border-left: #f0f0f0 1px solid; }

.hotkeys-message {
  color: red;
  margin-bottom: 8px; }

.add-defaults {
  float: right; }

.add-defaults-container {
  margin-bottom: 10px;
  cursor: pointer; }

.paste-mode-check {
  text-align: left;
  margin-left: 25%; }

.hotkey-field-hr {
  margin: 0px;
  width: 100%;
  border-color: #f0f0f0; }

.loader {
  border-radius: 50%;
  color: #02b3e4;
  font-size: 11px;
  text-indent: -99999em;
  margin: 25px auto;
  position: relative;
  width: 10em;
  height: 10em;
  box-shadow: inset 0 0 0 1em;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0); }
  .loader:before, .loader:after {
    border-radius: 50%; }
  .loader:before, .loader:after {
    position: absolute;
    content: ""; }
  .loader:before {
    width: 5.2em;
    height: 10.2em;
    background: white;
    border-radius: 10.2em 0 0 10.2em;
    top: -0.1em;
    left: -0.1em;
    -webkit-transform-origin: 5.2em 5.1em;
    transform-origin: 5.2em 5.1em;
    -webkit-animation: load2 2s infinite ease 1.5s;
    animation: load2 2s infinite ease 1.5s; }
  .loader:after {
    width: 5.2em;
    height: 10.2em;
    background: white;
    border-radius: 0 10.2em 10.2em 0;
    top: -0.1em;
    left: 5.1em;
    -webkit-transform-origin: 0px 5.1em;
    transform-origin: 0px 5.1em;
    -webkit-animation: load2 2s infinite ease;
    animation: load2 2s infinite ease; }

@-webkit-keyframes load2 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg); }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg); } }

@keyframes load2 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg); }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg); } }

.editor-navbar {
  display: none; }

.editor-container {
  border: none;
  background-color: #002b36; }
  .editor-container .navbar {
    position: absolute;
    bottom: 0;
    z-index: 2;
    width: 100%; }

.overflow-tab {
  background-color: #1c262f;
  height: 39px;
  width: 21px; }
  .overflow-tab:before {
    line-height: 40px;
    color: white; }

.overflow-dropdown {
  border-radius: 4px;
  top: 39px;
  padding: 3px 0;
  color: #2e3d49; }
  .overflow-dropdown li:hover, .overflow-dropdown li:active {
    background-color: #02ccba; }

/*

    Name:       udacity
    Author:     Jocelyn

    Original seti color scheme by Jesse Weed (https://github.com/jesseweed/seti-syntax)
    Original color scheme has been edited to match Udacity colors

*/
.cm-s-udacity.CodeMirror {
  background-color: #24323E;
  color: #DBE2E8;
  border: none; }

.cm-s-udacity .CodeMirror-wrap {
  /* enable rc-tooltip menu with z-index 1070 to render on top of this
   * tested in edge on windows10
   */
  z-index: 10; }

.cm-s-udacity .CodeMirror-gutters {
  color: #95ADC1;
  background-color: #24323E;
  border: none; }

.cm-s-udacity .CodeMirror-cursor {
  border-left: solid 2px #02B3E4; }

.cm-s-udacity .CodeMirror-linenumber {
  color: #95ADC1;
  line-height: 24px; }

.cm-s-udacity pre.CodeMirror-line {
  font-family: "source-code-pro", monospace;
  font-size: 14px;
  line-height: 24px; }

.cm-s-udacity .CodeMirror-lines {
  padding: 0px; }

.cm-s-udacity.CodeMirror-focused div.CodeMirror-selected {
  background: #3A4F5F; }

.cm-s-udacity .CodeMirror-line::selection, .cm-s-udacity .CodeMirror-line > span::selection, .cm-s-udacity .CodeMirror-line > span > span::selection {
  background: rgba(255, 255, 255, 0.1); }

.cm-s-udacity .CodeMirror-line::-moz-selection, .cm-s-udacity .CodeMirror-line > span::-moz-selection, .cm-s-udacity .CodeMirror-line > span > span::-moz-selection {
  background: rgba(255, 255, 255, 0.1); }

.cm-s-udacity span.cm-comment {
  color: #7D97AD; }

.cm-s-udacity span.cm-string, .cm-s-udacity span.cm-string-2 {
  color: #D38BFF; }

.cm-s-udacity span.cm-number {
  color: #FF7D7D; }

.cm-s-udacity span.cm-variable {
  color: #DBE2E8; }

.cm-s-udacity span.cm-variable-2 {
  color: #02CCBA; }

.cm-s-udacity span.cm-def {
  color: #D38BFF; }

.cm-s-udacity span.cm-keyword {
  color: #ff79c6; }

.cm-s-udacity span.cm-operator {
  color: #9fca56; }

.cm-s-udacity span.cm-keyword {
  color: #e6cd69; }

.cm-s-udacity span.cm-atom {
  color: #FF7D7D; }

.cm-s-udacity span.cm-meta {
  color: #D38BFF; }

.cm-s-udacity span.cm-tag {
  color: #D38BFF; }

.cm-s-udacity span.cm-attribute {
  color: #9fca56; }

.cm-s-udacity span.cm-qualifier {
  color: #9fca56; }

.cm-s-udacity span.cm-property {
  color: #02CCBA; }

.cm-s-udacity span.cm-variable-3, .cm-s-udacity span.cm-type {
  color: #9fca56; }

.cm-s-udacity span.cm-builtin {
  color: #9fca56; }

.cm-s-udacity .CodeMirror-activeline-background {
  background: #344655; }

.cm-s-udacity .CodeMirror-matchingbracket {
  text-decoration: underline;
  color: white !important; }

/* Make tabs visible.  See http://codemirror.net/demo/visibletabs.html */
.cm-s-udacity span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAYElEQVRIx+2UMQ6AMAwDzwixdGBgqAT//xojW2cz0MIbgnJLFHmJZSuQJP/HtmxX20vfj6FNEQxIMtCAYeK9e7a9BwpDQO3zMSDpDFKjAmw9iRKqQrYFrECTdOVXSJKPG893HnQdCN1BAAAAAElFTkSuQmCC);
  background-position: right;
  background-repeat: no-repeat; }

/* class-web styles/app.scss overrides cm defaults making search text unreadable */
.cm-s-udacity.CodeMirror.CodeMirror-wrap .CodeMirror-dialog
input:not([type=button]):not([type=submit]):not([type=checkbox]):not([type=radio]):not([role=combobox]) {
  /* copied from codemirror/addon/dialog.css#.CodeMirror-dialog */
  border: none;
  outline: none;
  background: transparent;
  width: 20em;
  color: inherit;
  font-family: monospace;
  /* added to override additional styles */
  box-shadow: none; }

/* overrides cm default yellowish highlighting of terms that match search */
.cm-s-udacity .cm-searching {
  background-color: #02b3e4; }
</style><style type="text/css">/* BASICS */

.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  font-family: monospace;
  height: 300px;
  color: black;
  direction: ltr;
}

/* PADDING */

.CodeMirror-lines {
  padding: 4px 0; /* Vertical padding around content */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  padding: 0 4px; /* Horizontal padding of content */
}

.CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  background-color: white; /* The little square between H and V scrollbars */
}

/* GUTTER */

.CodeMirror-gutters {
  border-right: 1px solid #ddd;
  background-color: #f7f7f7;
  white-space: nowrap;
}
.CodeMirror-linenumbers {}
.CodeMirror-linenumber {
  padding: 0 3px 0 5px;
  min-width: 20px;
  text-align: right;
  color: #999;
  white-space: nowrap;
}

.CodeMirror-guttermarker { color: black; }
.CodeMirror-guttermarker-subtle { color: #999; }

/* CURSOR */

.CodeMirror-cursor {
  border-left: 1px solid black;
  border-right: none;
  width: 0;
}
/* Shown when moving in bi-directional text */
.CodeMirror div.CodeMirror-secondarycursor {
  border-left: 1px solid silver;
}
.cm-fat-cursor .CodeMirror-cursor {
  width: auto;
  border: 0 !important;
  background: #7e7;
}
.cm-fat-cursor div.CodeMirror-cursors {
  z-index: 1;
}
.cm-fat-cursor-mark {
  background-color: rgba(20, 255, 20, 0.5);
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
}
.cm-animate-fat-cursor {
  width: auto;
  border: 0;
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
  background-color: #7e7;
}
@-moz-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@-webkit-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}

/* Can style cursor different in overwrite (non-insert) mode */
.CodeMirror-overwrite .CodeMirror-cursor {}

.cm-tab { display: inline-block; text-decoration: inherit; }

.CodeMirror-rulers {
  position: absolute;
  left: 0; right: 0; top: -50px; bottom: 0;
  overflow: hidden;
}
.CodeMirror-ruler {
  border-left: 1px solid #ccc;
  top: 0; bottom: 0;
  position: absolute;
}

/* DEFAULT THEME */

.cm-s-default .cm-header {color: blue;}
.cm-s-default .cm-quote {color: #090;}
.cm-negative {color: #d44;}
.cm-positive {color: #292;}
.cm-header, .cm-strong {font-weight: bold;}
.cm-em {font-style: italic;}
.cm-link {text-decoration: underline;}
.cm-strikethrough {text-decoration: line-through;}

.cm-s-default .cm-keyword {color: #708;}
.cm-s-default .cm-atom {color: #219;}
.cm-s-default .cm-number {color: #164;}
.cm-s-default .cm-def {color: #00f;}
.cm-s-default .cm-variable,
.cm-s-default .cm-punctuation,
.cm-s-default .cm-property,
.cm-s-default .cm-operator {}
.cm-s-default .cm-variable-2 {color: #05a;}
.cm-s-default .cm-variable-3, .cm-s-default .cm-type {color: #085;}
.cm-s-default .cm-comment {color: #a50;}
.cm-s-default .cm-string {color: #a11;}
.cm-s-default .cm-string-2 {color: #f50;}
.cm-s-default .cm-meta {color: #555;}
.cm-s-default .cm-qualifier {color: #555;}
.cm-s-default .cm-builtin {color: #30a;}
.cm-s-default .cm-bracket {color: #997;}
.cm-s-default .cm-tag {color: #170;}
.cm-s-default .cm-attribute {color: #00c;}
.cm-s-default .cm-hr {color: #999;}
.cm-s-default .cm-link {color: #00c;}

.cm-s-default .cm-error {color: #f00;}
.cm-invalidchar {color: #f00;}

.CodeMirror-composing { border-bottom: 2px solid; }

/* Default styles for common addons */

div.CodeMirror span.CodeMirror-matchingbracket {color: #0b0;}
div.CodeMirror span.CodeMirror-nonmatchingbracket {color: #a22;}
.CodeMirror-matchingtag { background: rgba(255, 150, 0, .3); }
.CodeMirror-activeline-background {background: #e8f2ff;}

/* STOP */

/* The rest of this file contains styles related to the mechanics of
   the editor. You probably shouldn't touch them. */

.CodeMirror {
  position: relative;
  overflow: hidden;
  background: white;
}

.CodeMirror-scroll {
  overflow: scroll !important; /* Things will break if this is overridden */
  /* 30px is the magic margin used to hide the element's real scrollbars */
  /* See overflow: hidden in .CodeMirror */
  margin-bottom: -30px; margin-right: -30px;
  padding-bottom: 30px;
  height: 100%;
  outline: none; /* Prevent dragging from highlighting the element */
  position: relative;
}
.CodeMirror-sizer {
  position: relative;
  border-right: 30px solid transparent;
}

/* The fake, visible scrollbars. Used to force redraw during scrolling
   before actual scrolling happens, thus preventing shaking and
   flickering artifacts. */
.CodeMirror-vscrollbar, .CodeMirror-hscrollbar, .CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  position: absolute;
  z-index: 6;
  display: none;
}
.CodeMirror-vscrollbar {
  right: 0; top: 0;
  overflow-x: hidden;
  overflow-y: scroll;
}
.CodeMirror-hscrollbar {
  bottom: 0; left: 0;
  overflow-y: hidden;
  overflow-x: scroll;
}
.CodeMirror-scrollbar-filler {
  right: 0; bottom: 0;
}
.CodeMirror-gutter-filler {
  left: 0; bottom: 0;
}

.CodeMirror-gutters {
  position: absolute; left: 0; top: 0;
  min-height: 100%;
  z-index: 3;
}
.CodeMirror-gutter {
  white-space: normal;
  height: 100%;
  display: inline-block;
  vertical-align: top;
  margin-bottom: -30px;
}
.CodeMirror-gutter-wrapper {
  position: absolute;
  z-index: 4;
  background: none !important;
  border: none !important;
}
.CodeMirror-gutter-background {
  position: absolute;
  top: 0; bottom: 0;
  z-index: 4;
}
.CodeMirror-gutter-elt {
  position: absolute;
  cursor: default;
  z-index: 4;
}
.CodeMirror-gutter-wrapper ::selection { background-color: transparent }
.CodeMirror-gutter-wrapper ::-moz-selection { background-color: transparent }

.CodeMirror-lines {
  cursor: text;
  min-height: 1px; /* prevents collapsing before first draw */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  /* Reset some styles that the rest of the page might have set */
  -moz-border-radius: 0; -webkit-border-radius: 0; border-radius: 0;
  border-width: 0;
  background: transparent;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
  white-space: pre;
  word-wrap: normal;
  line-height: inherit;
  color: inherit;
  z-index: 2;
  position: relative;
  overflow: visible;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-variant-ligatures: contextual;
  font-variant-ligatures: contextual;
}
.CodeMirror-wrap pre.CodeMirror-line,
.CodeMirror-wrap pre.CodeMirror-line-like {
  word-wrap: break-word;
  white-space: pre-wrap;
  word-break: normal;
}

.CodeMirror-linebackground {
  position: absolute;
  left: 0; right: 0; top: 0; bottom: 0;
  z-index: 0;
}

.CodeMirror-linewidget {
  position: relative;
  z-index: 2;
  padding: 0.1px; /* Force widget margins to stay inside of the container */
}

.CodeMirror-widget {}

.CodeMirror-rtl pre { direction: rtl; }

.CodeMirror-code {
  outline: none;
}

/* Force content-box sizing for the elements where we expect it */
.CodeMirror-scroll,
.CodeMirror-sizer,
.CodeMirror-gutter,
.CodeMirror-gutters,
.CodeMirror-linenumber {
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}

.CodeMirror-measure {
  position: absolute;
  width: 100%;
  height: 0;
  overflow: hidden;
  visibility: hidden;
}

.CodeMirror-cursor {
  position: absolute;
  pointer-events: none;
}
.CodeMirror-measure pre { position: static; }

div.CodeMirror-cursors {
  visibility: hidden;
  position: relative;
  z-index: 3;
}
div.CodeMirror-dragcursors {
  visibility: visible;
}

.CodeMirror-focused div.CodeMirror-cursors {
  visibility: visible;
}

.CodeMirror-selected { background: #d9d9d9; }
.CodeMirror-focused .CodeMirror-selected { background: #d7d4f0; }
.CodeMirror-crosshair { cursor: crosshair; }
.CodeMirror-line::selection, .CodeMirror-line > span::selection, .CodeMirror-line > span > span::selection { background: #d7d4f0; }
.CodeMirror-line::-moz-selection, .CodeMirror-line > span::-moz-selection, .CodeMirror-line > span > span::-moz-selection { background: #d7d4f0; }

.cm-searching {
  background-color: #ffa;
  background-color: rgba(255, 255, 0, .4);
}

/* Used to force a border model for a node */
.cm-force-border { padding-right: .1px; }

@media print {
  /* Hide the cursor when printing */
  .CodeMirror div.CodeMirror-cursors {
    visibility: hidden;
  }
}

/* See issue #2901 */
.cm-tab-wrap-hack:after { content: ''; }

/* Help users use markselection to safely style text background */
span.CodeMirror-selectedtext { background: none; }
</style><style type="text/css">.CodeMirror-simplescroll-horizontal div, .CodeMirror-simplescroll-vertical div {
  position: absolute;
  background: #ccc;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  border: 1px solid #bbb;
  border-radius: 2px;
}

.CodeMirror-simplescroll-horizontal, .CodeMirror-simplescroll-vertical {
  position: absolute;
  z-index: 6;
  background: #eee;
}

.CodeMirror-simplescroll-horizontal {
  bottom: 0; left: 0;
  height: 8px;
}
.CodeMirror-simplescroll-horizontal div {
  bottom: 0;
  height: 100%;
}

.CodeMirror-simplescroll-vertical {
  right: 0; top: 0;
  width: 8px;
}
.CodeMirror-simplescroll-vertical div {
  right: 0;
  width: 100%;
}


.CodeMirror-overlayscroll .CodeMirror-scrollbar-filler, .CodeMirror-overlayscroll .CodeMirror-gutter-filler {
  display: none;
}

.CodeMirror-overlayscroll-horizontal div, .CodeMirror-overlayscroll-vertical div {
  position: absolute;
  background: #bcd;
  border-radius: 3px;
}

.CodeMirror-overlayscroll-horizontal, .CodeMirror-overlayscroll-vertical {
  position: absolute;
  z-index: 6;
}

.CodeMirror-overlayscroll-horizontal {
  bottom: 0; left: 0;
  height: 6px;
}
.CodeMirror-overlayscroll-horizontal div {
  bottom: 0;
  height: 100%;
}

.CodeMirror-overlayscroll-vertical {
  right: 0; top: 0;
  width: 6px;
}
.CodeMirror-overlayscroll-vertical div {
  right: 0;
  width: 100%;
}
</style><style type="text/css">.CodeMirror-foldmarker {
  color: blue;
  text-shadow: #b9f 1px 1px 2px, #b9f -1px -1px 2px, #b9f 1px -1px 2px, #b9f -1px 1px 2px;
  font-family: arial;
  line-height: .3;
  cursor: pointer;
}
.CodeMirror-foldgutter {
  width: .7em;
}
.CodeMirror-foldgutter-open,
.CodeMirror-foldgutter-folded {
  cursor: pointer;
}
.CodeMirror-foldgutter-open:after {
  content: "\25BE";
}
.CodeMirror-foldgutter-folded:after {
  content: "\25B8";
}
</style><style type="text/css">.CodeMirror-dialog {
  position: absolute;
  left: 0; right: 0;
  background: inherit;
  z-index: 15;
  padding: .1em .8em;
  overflow: hidden;
  color: inherit;
}

.CodeMirror-dialog-top {
  border-bottom: 1px solid #eee;
  top: 0;
}

.CodeMirror-dialog-bottom {
  border-top: 1px solid #eee;
  bottom: 0;
}

.CodeMirror-dialog input {
  border: none;
  outline: none;
  background: transparent;
  width: 20em;
  color: inherit;
  font-family: monospace;
}

.CodeMirror-dialog button {
  font-size: 70%;
}
</style><style type="text/css">/**
 * Copyright (c) 2014 The xterm.js authors. All rights reserved.
 * Copyright (c) 2012-2013, Christopher Jeffrey (MIT License)
 * https://github.com/chjj/term.js
 * @license MIT
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * Originally forked from (with the author's permission):
 *   Fabrice Bellard's javascript vt100 for jslinux:
 *   http://bellard.org/jslinux/
 *   Copyright (c) 2011 Fabrice Bellard
 *   The original design remains. The terminal itself
 *   has been extended to include xterm CSI codes, among
 *   other features.
 */

/**
 *  Default styles for xterm.js
 */

.xterm {
    font-feature-settings: "liga" 0;
    position: relative;
    user-select: none;
    -ms-user-select: none;
    -webkit-user-select: none;
}

.xterm.focus,
.xterm:focus {
    outline: none;
}

.xterm .xterm-helpers {
    position: absolute;
    top: 0;
    /**
     * The z-index of the helpers must be higher than the canvases in order for
     * IMEs to appear on top.
     */
    z-index: 10;
}

.xterm .xterm-helper-textarea {
    /*
     * HACK: to fix IE's blinking cursor
     * Move textarea out of the screen to the far left, so that the cursor is not visible.
     */
    position: absolute;
    opacity: 0;
    left: -9999em;
    top: 0;
    width: 0;
    height: 0;
    z-index: -10;
    /** Prevent wrapping so the IME appears against the textarea at the correct position */
    white-space: nowrap;
    overflow: hidden;
    resize: none;
}

.xterm .composition-view {
    /* TODO: Composition position got messed up somewhere */
    background: #000;
    color: #FFF;
    display: none;
    position: absolute;
    white-space: nowrap;
    z-index: 1;
}

.xterm .composition-view.active {
    display: block;
}

.xterm .xterm-viewport {
    /* On OS X this is required in order for the scroll bar to appear fully opaque */
    background-color: #000;
    overflow-y: scroll;
    cursor: default;
    position: absolute;
    right: 0;
    left: 0;
    top: 0;
    bottom: 0;
}

.xterm .xterm-screen {
    position: relative;
}

.xterm .xterm-screen canvas {
    position: absolute;
    left: 0;
    top: 0;
}

.xterm .xterm-scroll-area {
    visibility: hidden;
}

.xterm-char-measure-element {
    display: inline-block;
    visibility: hidden;
    position: absolute;
    top: 0;
    left: -9999em;
    line-height: normal;
}

.xterm {
    cursor: text;
}

.xterm.enable-mouse-events {
    /* When mouse events are enabled (eg. tmux), revert to the standard pointer cursor */
    cursor: default;
}

.xterm.xterm-cursor-pointer {
    cursor: pointer;
}

.xterm.column-select.focus {
    /* Column selection mode */
    cursor: crosshair;
}

.xterm .xterm-accessibility,
.xterm .xterm-message {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    right: 0;
    z-index: 100;
    color: transparent;
}

.xterm .live-region {
    position: absolute;
    left: -9999px;
    width: 1px;
    height: 1px;
    overflow: hidden;
}

.xterm-dim {
    opacity: 0.5;
}

.xterm-underline {
    text-decoration: underline;
}
</style><style type="text/css">.terminal.xterm .xterm-viewport {
  background-color: #24323E !important;
}
</style></head><body lang="en-US" dir="ltr"><div id="app"><div id="main"><style type="text/css">
#intercom-container {
  display: none;
}
</style><div class="content"><div data-test="nanodegree-container"><div><noscript></noscript><div><div class="_layout--large-nav--1elMR"><div class="_layout-module--container--3f2U4"><ul class="_layout-module--a11y-nav--vkRI0"><li><a href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/2457f366-d634-482e-9504-3eced80d87ab#content">Jump to content</a></li><li><a href="mailto:a11y@udacity.com?subject=Accessibility%20Support" target="_blank">Email for accessibility support</a></li></ul><nav class="_layout-module--nav--3qaiq _layout-module--secondary-only--33dGC _layout-module--hidden--2IaXy"><div class="_layout-module--nav-contents--3VsBp"><div id="main-layout-sidebar" class="_layout-module--secondary-nav--dElFh"><div data-test="lesson-sidebar"><div class="_sidebar--sidebar--1jCxg"><h3 class="_sidebar--header--2BaH_"><a href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309"><span class="_sidebar--title-content--tLGxZ"><span class="_sidebar--arrow--2Hns-"><i class="vds-icon vds-icon--lg" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M20.589 23.84l-10.175-7.13c-.422-.297-.541-.903-.265-1.356a.947.947 0 0 1 .276-.292L20.6 8.152c.425-.29.99-.153 1.259.304.092.157.141.338.141.524v14.04c0 .542-.409.98-.912.98a.868.868 0 0 1-.5-.16z" fill-rule="evenodd"></path></svg></i></span><span class="_sidebar--title--3HHFG text--nowrap-ellipsis--TMdB3"><span>Project:</span><span class="_sidebar--title-text--vcBON text--nowrap-ellipsis--TMdB3"> Create Your Own Image Classifier</span></span></span></a></h3><div class="_sidebar--sections--2TxEN"><div role="group" aria-expanded="false" class="_section--section--3V1-y shared--section--3e1zX _section--_hide-shadow--1yGng"><a href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/2457f366-d634-482e-9504-3eced80d87ab#" class="_section--header--hPsXJ shared--header--3QkFS"><h2>Search</h2><i class="vds-icon vds-icon--sm vds-color--silver" role="img"><span class="vds-visually-hidden">Search</span><svg viewBox="0 0 32 32"><path d="M21.176 19.762l4.531 4.53a1 1 0 0 1-1.414 1.415l-4.531-4.531a8.5 8.5 0 1 1 1.414-1.414zM14.5 21a6.5 6.5 0 1 0 0-13 6.5 6.5 0 0 0 0 13z" fill-rule="nonzero"></path></svg></i></a></div><div role="group" aria-expanded="false" class="_section--section--3V1-y shared--section--3e1zX _section--_hide-shadow--1yGng"><a href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/2457f366-d634-482e-9504-3eced80d87ab#" class="_section--header--hPsXJ shared--header--3QkFS"><h2>Resources</h2><span class="_section--expand--3Y-E2 shared--expand--239lE"><i class="vds-icon vds-icon--sm" role="img"><span class="vds-visually-hidden">Open</span><svg viewBox="0 0 32 32"><path d="M8.16 11.411l7.13 10.175c.297.422.903.541 1.356.265a.947.947 0 0 0 .292-.276l6.91-10.175c.29-.425.153-.99-.304-1.259A1.033 1.033 0 0 0 23.02 10H8.98c-.542 0-.98.409-.98.912 0 .178.055.351.16.5z" fill-rule="evenodd"></path></svg></i></span></a></div><div role="group" aria-expanded="true" class="_section--section-selected--24hRk shared--section-expanded--2eoTJ shared--section--3e1zX _section--_hide-shadow--1yGng"><a href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/2457f366-d634-482e-9504-3eced80d87ab#" aria-owns="tree-concepts" class="_section--header-expanded--2PtoU shared--header-expanded--290TG shared--header--3QkFS"><h2>Concepts</h2><span class="_section--collapse--3crCv shared--collapse--2w1x2"><i class="vds-icon vds-icon--sm" role="img"><span class="vds-visually-hidden">Close</span><svg viewBox="0 0 32 32"><path d="M8.16 11.411l7.13 10.175c.297.422.903.541 1.356.265a.947.947 0 0 0 .292-.276l6.91-10.175c.29-.425.153-.99-.304-1.259A1.033 1.033 0 0 0 23.02 10H8.98c-.542 0-.98.409-.98.912 0 .178.055.351.16.5z" fill-rule="evenodd"></path></svg></i></span></a><div id="tree-concepts"><ol class="index--contents-list--33vHB"><li id="contents-list-scroll-target-89202d47-2620-41e7-8caa-31df5a0f7eab" class="_item--item--dTIux"><a title="1. Instructor" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/89202d47-2620-41e7-8caa-31df5a0f7eab"><span class="_item--waypoint-check--nmzcM"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M7.707 17.093a1 1 0 0 0-1.414 1.414l7.2 7.2a1 1 0 0 0 1.564-.192l10.8-18a1 1 0 1 0-1.714-1.03L14 23.388l-6.294-6.294z" fill-rule="nonzero"></path></svg></i></span> 1. Instructor</a></li><li id="contents-list-scroll-target-84d42c50-f836-479c-9f42-b26eb14e409f" class="_item--item--dTIux"><a title="2. Project Intro" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/84d42c50-f836-479c-9f42-b26eb14e409f"><span class="_item--waypoint-check--nmzcM"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M7.707 17.093a1 1 0 0 0-1.414 1.414l7.2 7.2a1 1 0 0 0 1.564-.192l10.8-18a1 1 0 1 0-1.714-1.03L14 23.388l-6.294-6.294z" fill-rule="nonzero"></path></svg></i></span> 2. Project Intro</a></li><li id="contents-list-scroll-target-8b7e602a-4a29-4009-b162-73c6051d4647" class="_item--item--dTIux"><a title="3. Introduction to GPU Workspaces" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/8b7e602a-4a29-4009-b162-73c6051d4647"><span class="_item--waypoint-check--nmzcM"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M7.707 17.093a1 1 0 0 0-1.414 1.414l7.2 7.2a1 1 0 0 0 1.564-.192l10.8-18a1 1 0 1 0-1.714-1.03L14 23.388l-6.294-6.294z" fill-rule="nonzero"></path></svg></i></span> 3. Introduction to GPU Workspaces</a></li><li id="contents-list-scroll-target-d209dda2-cf59-4cd1-b193-45b84e472f42" class="_item--item--dTIux"><a title="4. Updating to PyTorch v0.4" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/d209dda2-cf59-4cd1-b193-45b84e472f42"><span class="_item--waypoint-check--nmzcM"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M7.707 17.093a1 1 0 0 0-1.414 1.414l7.2 7.2a1 1 0 0 0 1.564-.192l10.8-18a1 1 0 1 0-1.714-1.03L14 23.388l-6.294-6.294z" fill-rule="nonzero"></path></svg></i></span> 4. Updating to PyTorch v0.4</a></li><li id="contents-list-scroll-target-a0638042-7d4c-4e3e-9d19-c71e6a87fe18" class="_item--item--dTIux"><a title="5. Image Classifier - Part 1 - Development" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/a0638042-7d4c-4e3e-9d19-c71e6a87fe18"><span class="_item--waypoint-check--nmzcM"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M7.707 17.093a1 1 0 0 0-1.414 1.414l7.2 7.2a1 1 0 0 0 1.564-.192l10.8-18a1 1 0 1 0-1.714-1.03L14 23.388l-6.294-6.294z" fill-rule="nonzero"></path></svg></i></span> 5. Image Classifier - Part 1 - Development</a></li><li id="contents-list-scroll-target-313e2076-4626-4650-906a-ec82eb61c00e" class="_item--item--dTIux"><a title="6. Image Classifier - Part 1 - Workspace" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/313e2076-4626-4650-906a-ec82eb61c00e"><span class="_item--waypoint-check--nmzcM"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M7.707 17.093a1 1 0 0 0-1.414 1.414l7.2 7.2a1 1 0 0 0 1.564-.192l10.8-18a1 1 0 1 0-1.714-1.03L14 23.388l-6.294-6.294z" fill-rule="nonzero"></path></svg></i></span> 6. Image Classifier - Part 1 - Workspace</a></li><li id="contents-list-scroll-target-4db448a2-9b6c-4df8-9685-d905814bca04" class="_item--item--dTIux"><a title="7. Image Classifier - Part 2 - Command Line App" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/4db448a2-9b6c-4df8-9685-d905814bca04"><span class="_item--waypoint-check--nmzcM"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M7.707 17.093a1 1 0 0 0-1.414 1.414l7.2 7.2a1 1 0 0 0 1.564-.192l10.8-18a1 1 0 1 0-1.714-1.03L14 23.388l-6.294-6.294z" fill-rule="nonzero"></path></svg></i></span> 7. Image Classifier - Part 2 - Command Line App</a></li><li id="contents-list-scroll-target-2457f366-d634-482e-9504-3eced80d87ab" class="_item--item-selected--3LMMf"><a title="8. Image Classifier - Part 2 - Workspace" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/2457f366-d634-482e-9504-3eced80d87ab"><span class="_item--waypoint-check--nmzcM"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M7.707 17.093a1 1 0 0 0-1.414 1.414l7.2 7.2a1 1 0 0 0 1.564-.192l10.8-18a1 1 0 1 0-1.714-1.03L14 23.388l-6.294-6.294z" fill-rule="nonzero"></path></svg></i></span> 8. Image Classifier - Part 2 - Workspace</a></li><li id="contents-list-scroll-target-b4162538-0215-4bd0-9357-5e1614028ccf" class="_item--item--dTIux"><a title="9. Rubric" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/b4162538-0215-4bd0-9357-5e1614028ccf"><span class="_item--waypoint-check--nmzcM"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M7.707 17.093a1 1 0 0 0-1.414 1.414l7.2 7.2a1 1 0 0 0 1.564-.192l10.8-18a1 1 0 1 0-1.714-1.03L14 23.388l-6.294-6.294z" fill-rule="nonzero"></path></svg></i></span> 9. Rubric</a></li><li id="contents-list-scroll-target-7e88bcd6-600e-4edb-af44-3bc4e695951c" class="_item--item--dTIux"><a title="10. Project: Create Your Own Image Classifier" href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/project"><span class="_item--waypoint-star--1dLwl"><i class="vds-icon vds-icon--sm" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M15.794 23.048l-5.63 2.852a1 1 0 0 1-1.436-1.067l1.066-5.987-4.479-4.207a1 1 0 0 1 .546-1.72l6.224-.87 2.819-5.505a1 1 0 0 1 1.78 0l2.818 5.504 6.224.872a1 1 0 0 1 .546 1.719l-4.478 4.207 1.065 5.987a1 1 0 0 1-1.437 1.067l-5.628-2.852z" fill-rule="nonzero"></path></svg></i></span> 10. Project: Create Your Own Image Classifier</a></li></ol></div></div></div><div class="_sidebar--footer--2i1oy"><ul class="_service-links--service-links--25Cft"><li><a role="link" tabindex="0" class="_service-links--service-link-item--1qvdY"><span class="_service-links--glyph-wrapper--2tXod _service-links--knowledge--2IhC7"><i class="vds-icon" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M17.732 27a2 2 0 0 1-3.464 0H14a2 2 0 0 1-2-2v-3.936a9 9 0 1 1 8 0V25a2 2 0 0 1-2 2h-.268zM18 22v-1h-4v1h4zm0 2h-4v1h4v-1zm-5.61-5h7.22a7 7 0 1 0-7.218 0zM16 8a1 1 0 0 1 0 2 3 3 0 0 0-3 3 1 1 0 0 1-2 0 5 5 0 0 1 5-5z" fill-rule="nonzero"></path></svg></i></span><span class="_service-links--service-title--2KAOW">Mentor Help</span><span class="_service-links--service-description--2JMqH">Ask a mentor on our Q&amp;A platform</span></a></li><li><div class="index--studenthub-link-wrapper--3rL8o"><a role="link" tabindex="0" class="index--service-link-item--1Wfk-"><span class="index--glyph-wrapper--1SjGA index--student-hub--2n2zu index--studenthub-btn--2jSGs lesson"><i class="vds-icon" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M12 10.397V9a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3h-2v3.397a3 3 0 0 1-3 3H9.823l-4.325 2.471a1 1 0 0 1-1.486-1.01l.99-6.93v-5.531a3 3 0 0 1 3-3H12zM23 16h2a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1H15a1 1 0 0 0-1 1v1.397h6a3 3 0 0 1 3 3V16zM6.99 19.141l-.71 4.976 2.78-1.588a1 1 0 0 1 .496-.132h10.445a1 1 0 0 0 1-1v-8a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1V19l-.01.141z" fill-rule="nonzero"></path></svg></i></span><span class="index--service-title--3qRug">Peer Chat</span><span class="index--service-description--190Zi">Chat with peers and alumni</span></a><div class="index--lesson--1F_xH index--_badge--1WlOE"><span title="Notification" class="notification-badge--notificationOuter--9OFHB"><span title="Unread messages" class="notification-badge--notificationInner--2y0Oa"></span></span></div></div></li></ul></div></div></div></div></div></nav><main class="_layout-module--main--20EWg"><div class="_layout-module--title-area--1yynf"><div class="_header-module--header--1boX-"><div><div data-test="concept-header"><nav class="index--dark-header--2SHyn index--_header--36qYf"><div class="vds-flex vds-flex--align-center vds-flex--full vds-flex--justify-between vds-flex--spacing-2x"><div class="vds-flex__item"><div class="hamburger--hamburger--1oS_7 index--hamburger--31PjM"><a href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/2457f366-d634-482e-9504-3eced80d87ab#" class="hamburger--hamburger-link--3-KRS"><i class="vds-icon vds-color--cerulean" role="img"><span class="vds-visually-hidden">Toggle Sidebar</span><svg viewBox="0 0 32 32"><path d="M8 23a1 1 0 0 1 0-2h16a1 1 0 0 1 0 2H8zm0-6a1 1 0 0 1 0-2h16a1 1 0 0 1 0 2H8zm0-6a1 1 0 0 1 0-2h16a1 1 0 0 1 0 2H8z" fill-rule="nonzero"></path></svg></i></a></div></div><div class="vds-flex__item"><h1 id="header-title" aria-live="assertive">Image Classifier - Part 2 - Workspace</h1></div><div class="vds-flex__item"><div class="_header--right-node--tOqX9"><div><span class="index--from-tablet--cciH6"><button class="vds-button vds-button--minimal vds-button--small" aria-busy="false" type="button"><span class="vds-button__content">Send Feedback</span></button></span><span class="index--until-tablet--3TJ_9"><button class="vds-button vds-button--minimal vds-button__icon vds-button__icon--only" aria-busy="false" type="button"><span class="vds-button__content"><i class="vds-icon vds-color--cerulean" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M18.245 16.566L16.6 17.8a1 1 0 0 1-1.2 0l-1.6-1.2a1.009 1.009 0 0 1-.093.107l-2 2a1 1 0 0 1-1.414-1.414l1.899-1.9-4.193-3.143L8 20.998 24.001 21 24 12.25l-4.196 3.147 1.903 1.896a1 1 0 0 1-1.414 1.414l-2.1-2.102.052-.039zM9.667 11L16 15.75l6.33-4.748L9.667 11zM6 11.002C6 9.9 6.89 9 7.993 9h16.014C25.108 9 26 9.904 26 11.002v9.996C26 22.1 25.11 23 24.007 23H7.993A2.002 2.002 0 0 1 6 20.998v-9.996z" fill-rule="nonzero"></path></svg></i><span class="vds-visually-hidden"></span></span></button></span></div></div></div></div></nav></div></div></div></div><div class="_layout-module--content-area--tGmoA" style="background-color: rgb(250, 251, 252);"><div aria-hidden="true" class="_layout-module--hidden-header--3JZ5t"><div class="_header-module--header--1boX-"><div><div data-test="concept-header"><nav class="index--dark-header--2SHyn index--_header--36qYf"><div class="vds-flex vds-flex--align-center vds-flex--full vds-flex--justify-between vds-flex--spacing-2x"><div class="vds-flex__item"><div class="hamburger--hamburger--1oS_7 index--hamburger--31PjM"><a href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/2457f366-d634-482e-9504-3eced80d87ab#" class="hamburger--hamburger-link--3-KRS"><i class="vds-icon vds-color--cerulean" role="img"><span class="vds-visually-hidden">Toggle Sidebar</span><svg viewBox="0 0 32 32"><path d="M8 23a1 1 0 0 1 0-2h16a1 1 0 0 1 0 2H8zm0-6a1 1 0 0 1 0-2h16a1 1 0 0 1 0 2H8zm0-6a1 1 0 0 1 0-2h16a1 1 0 0 1 0 2H8z" fill-rule="nonzero"></path></svg></i></a></div></div><div class="vds-flex__item"><h1 id="header-title" aria-live="assertive">Image Classifier - Part 2 - Workspace</h1></div><div class="vds-flex__item"><div class="_header--right-node--tOqX9"><div><span class="index--from-tablet--cciH6"><button class="vds-button vds-button--minimal vds-button--small" aria-busy="false" type="button"><span class="vds-button__content">Send Feedback</span></button></span><span class="index--until-tablet--3TJ_9"><button class="vds-button vds-button--minimal vds-button__icon vds-button__icon--only" aria-busy="false" type="button"><span class="vds-button__content"><i class="vds-icon vds-color--cerulean" role="img" aria-hidden="true"><svg viewBox="0 0 32 32"><path d="M18.245 16.566L16.6 17.8a1 1 0 0 1-1.2 0l-1.6-1.2a1.009 1.009 0 0 1-.093.107l-2 2a1 1 0 0 1-1.414-1.414l1.899-1.9-4.193-3.143L8 20.998 24.001 21 24 12.25l-4.196 3.147 1.903 1.896a1 1 0 0 1-1.414 1.414l-2.1-2.102.052-.039zM9.667 11L16 15.75l6.33-4.748L9.667 11zM6 11.002C6 9.9 6.89 9 7.993 9h16.014C25.108 9 26 9.904 26 11.002v9.996C26 22.1 25.11 23 24.007 23H7.993A2.002 2.002 0 0 1 6 20.998v-9.996z" fill-rule="nonzero"></path></svg></i><span class="vds-visually-hidden"></span></span></button></span></div></div></div></div></nav></div></div></div></div><div id="content"></div><div id="main-layout-content" aria-labelledby="header-title" class="_body-module--body--UXv_5"><div data-test="concept-main" class="_main--main-wide--3IuxV _main--main--3mpPA"><div class="_main--content-container--ILkoI"><div><div class="index--container-wide--2OK8C"><div class="index--atom-wide--mz8j2 layout--content-wide--tivIS layout--content--3Smmq"><div style="height: calc(100vh - 57px);"><div class="blueprint-fullscreen--wrapper--2voit"><div style="height: 100%; position: relative;"><div class="scoped-bootstrap student-workspace " style="position: relative; height: calc(100% - 48px);"><div class="theme_dark" data-test="web-terminal-client" style="height: 100%;"><div id="layout" style="height: 100%;"><div id="layout_main" style="height: 100%;"><div class="panel files-panel" id="d1f2aa32-d607-458c-9d59-38f305e4bc63" style="left: 0%; right: 83.375%; top: 0%; bottom: 0%;">
<div id="files_container_inner">
  <div id="navbar_container"><div id="files_navbar" class="navbar unselectable button-navbar"><menu id="files_toolbar" class="nav navbar-nav unselectable"><li class="navigate_up"><a><span class="ureact-glyph-module--icon-arrow-left-sm--1Wem1 ureact-glyph-module--icon--1oZQL" title="Back"><i>Back</i></span></a></li><li><a data-test="wtc-add-file-menu"><span class="ureact-glyph-module--icon-add-sm--1fhrf ureact-glyph-module--icon--1oZQL" title="Add File"><i>Add File</i></span></a></li></menu></div></div>

  <ul id="myCrumbs" class="breadcrumbs"><li><a style="cursor: pointer;">/</a><span class="divider">&gt;</span></li><li class="active">home</li></ul>

  <div id="myFiles" class="files-table-wrapper"><table id="react-file-list" class="table table-condensed files-table"><tbody class="files_list"><tr class="files_list file_tab_link" data-name="backups" data-crumbs="/,home" data-is-dir="true"><td class="file_name"><a><span class="ureact-glyph-module--icon-folder-sm--2uHZW ureact-glyph-module--icon--1oZQL" title="folder-sm" style="color: rgb(125, 151, 173);"><i>folder-sm</i></span><span class="file_name_text">backups</span></a></td></tr><tr class="files_list file_tab_link" data-name="workspace" data-crumbs="/,home" data-is-dir="true"><td class="file_name"><a><span class="ureact-glyph-module--icon-folder-sm--2uHZW ureact-glyph-module--icon--1oZQL" title="folder-sm" style="color: rgb(125, 151, 173);"><i>folder-sm</i></span><span class="file_name_text">workspace</span></a></td></tr></tbody></table></div>

  <div id="upload_alerts"></div>
  <div id="upload_list"></div>
</div>
</div><div class="panel" id="277f6ed3-85e5-40b3-8e4d-240c6d42e4dd" style="left: 16.625%; right: 0%; top: 0%; bottom: 50%;">
    <div class="editor-tabs-wrapper">
      <div class="editor-tabs tab_bar unselectable"><div class="tab active"><span class="editor_tab"><span class="editor_tab_text">train.py</span><span class="editor_tab_members">1</span><span class="closetab">×</span></span></div><div class="tab"><span class="editor_tab"><span class="editor_tab_text">predict.py</span><span class="editor_tab_members">0</span><span class="closetab">×</span></span></div></div>
      <div class="overflow-tab editor_tab" style=""></div>
    </div>
    <ul class="overflow-dropdown hidden"></ul>
    <div class="editor">
      <div class="editor-loading hidden">
      </div>
      <div class="editor-empty empty_panel" style="display: none;">
        <div class="empty_icon editor"></div>
        <div class="empty_message">No Open Files</div><a href="https://classroom.udacity.com/nanodegrees/nd089-ent/parts/145b9557-e6d9-4bad-a8d9-26ab8e27e309/modules/55680ef0-9644-4ca9-b162-f6928674ad72/lessons/97c1b4fb-8cfb-40da-b2db-a7cf1a944939/concepts/2457f366-d634-482e-9504-3eced80d87ab#" class="empty_newtab">OPEN FILE</a>
      </div>
    <div class="CodeMirror cm-s-udacity CodeMirror-wrap CodeMirror-overlayscroll" style="width: 1332px; height: 100%;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 46px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-overlayscroll-horizontal" cm-not-content="true" style="display: none;"><div></div></div><div class="CodeMirror-overlayscroll-vertical" cm-not-content="true" style="display: block; bottom: 0px;"><div style="height: 10px; top: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 42px; margin-bottom: -17px; border-right-width: 13px; min-height: 19530px; padding-right: 6px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><div class="CodeMirror-linenumber CodeMirror-gutter-elt"><div>186</div></div></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 18px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: -42px; width: 42px;"></div><div class="CodeMirror-gutter-wrapper CodeMirror-activeline-gutter" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># Imports</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">2</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">argparse</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">3</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">numpy</span> <span class="cm-keyword">as</span> <span class="cm-variable">np</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">4</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">pandas</span> <span class="cm-keyword">as</span> <span class="cm-variable">pd</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">5</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">matplotlib</span>.<span class="cm-property">pyplot</span> <span class="cm-keyword">as</span> <span class="cm-variable">plt</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">6</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">torch</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">7</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">8</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">torch</span> <span class="cm-keyword">import</span> <span class="cm-variable">nn</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">9</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">torch</span> <span class="cm-keyword">import</span> <span class="cm-variable">optim</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">10</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">torch</span>.<span class="cm-property">nn</span>.<span class="cm-property">functional</span> <span class="cm-keyword">as</span> <span class="cm-variable">F</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">11</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">torchvision</span> <span class="cm-keyword">import</span> <span class="cm-variable">datasets</span>, <span class="cm-variable">transforms</span>, <span class="cm-variable">models</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">12</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">PIL</span> <span class="cm-keyword">import</span> <span class="cm-variable">Image</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">13</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">json</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">14</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">15</div><div class="CodeMirror-gutter-elt" style="left: 32px; width: 10px;"><div class="CodeMirror-foldgutter-open CodeMirror-guttermarker-subtle"></div></div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">main</span>():</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">16</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">17</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-comment"># get arguments from command line</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">18</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-builtin">input</span> <span class="cm-operator">=</span> <span class="cm-variable">get_args</span>()</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">19</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">20</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">path_to_image</span> <span class="cm-operator">=</span> <span class="cm-builtin">input</span>.<span class="cm-property">image_path</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">21</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">checkpt</span> <span class="cm-operator">=</span> <span class="cm-builtin">input</span>.<span class="cm-property">checkpoint</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">22</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">num</span> <span class="cm-operator">=</span> <span class="cm-builtin">input</span>.<span class="cm-property">top_k</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -42px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 24px;">23</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">cat_names</span> <span class="cm-operator">=</span> <span class="cm-builtin">input</span>.<span class="cm-property">category_names</span></span></pre></div></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 19530px;"></div><div class="CodeMirror-gutters" style="height: 19543px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 32px;"></div><div class="CodeMirror-gutter CodeMirror-foldgutter"></div></div></div></div><div class="CodeMirror cm-s-udacity CodeMirror-wrap CodeMirror-overlayscroll" style="display: none;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 0px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-overlayscroll-horizontal" cm-not-content="true" style="display: none;"><div></div></div><div class="CodeMirror-overlayscroll-vertical" cm-not-content="true" style="display: block; bottom: 0px;"><div style="height: 10px; top: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 39px; margin-bottom: -17px; border-right-width: 13px; min-height: 18px; padding-right: 6px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"></div><div class="CodeMirror-code" role="presentation"><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: -39px; width: 39px;"></div><div class="CodeMirror-gutter-wrapper CodeMirror-activeline-gutter" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 18px;"></div><div class="CodeMirror-gutters" style="height: 31px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 29px;"></div><div class="CodeMirror-gutter CodeMirror-foldgutter"></div></div></div></div></div>
  </div><div dir="ltr" class="panel style--terminal-panel--3mRAj" id="d428165b-feed-4100-861d-55d0ac3dc59f" style="left: 16.625%; right: 0%; top: 50%; bottom: 0%;"><div class="style--tabs-wrapper--3Ivkf"><div class="style--tabs--3jK2W"><div class="style--tab--3lebE style--plus--3gcff"><span>+</span></div></div><div class="style--tab-contents--31b94"><div class="style--tab-inner--RWmvF style--empty-tab--2N2Sa" style="z-index: 0;"><div class="style--empty--2mPvT"><div class="style--icon--2r5VQ"></div><div class="style--message--2r1uT">No Open Terminals</div><span class="style--new--3KX6E">NEW TERMINAL</span></div></div></div></div></div><div id="94e2c020-1efd-4bc9-b1d4-5ae1d76e026e" class="panel results running" style="display: none;"><div class="grading--drawer-toggle--2npgm"><div data-test="hide-grader" class="grading--close--2Ib1y"><span class="ureact-glyph-module--icon-arrow-down-sm--M04mg ureact-glyph-module--icon--1oZQL" title=""><i></i></span><span class="grading--hide--1bOok">HIDE GRADER</span></div></div><div class="grading--main--2Jevc"><div class="grading--results-container--1vFQg"><div class="grading--icon-container--IIfrY"><span class="grading--loading-icon--JMN0H grading--icon--2Y34y"></span></div><div class="grading--results--2iW_a"><div class="grading--results-header--1uXap"><h2 class="grading--results-title--4Z-cK">Checking your work for completion.</h2></div><div class="grading--results-details--1PXuG">This may take a few minutes. Thanks for your patience!</div></div></div></div></div><div id="split_x0" class="resize resize_x split_right_d1f2aa32-d607-458c-9d59-38f305e4bc63 split_left_split_x1_y0 split_left_277f6ed3-85e5-40b3-8e4d-240c6d42e4dd split_left_d428165b-feed-4100-861d-55d0ac3dc59f ui-draggable ui-draggable-handle" style="left: 16.625%; right: auto; top: 0%; bottom: 0%;"></div><div id="split_x1_y0" class="resize resize_y split_bottom_277f6ed3-85e5-40b3-8e4d-240c6d42e4dd split_top_d428165b-feed-4100-861d-55d0ac3dc59f ui-draggable ui-draggable-handle" style="left: 16.625%; right: 0%; top: 50%; bottom: auto;"></div></div></div></div></div><div data-test="control-bar" class="control-bar--control-bar--xQofX"><div class="control-bar--menu-left--39Mzn"><div class="control-bar--left-group--3GkAw"><div class="control-bar--left-group-upper--2R8zc"><div class="control-bar--tooltip-container--16Pyl"><span class="control-bar--up-arrow--4z9Yd"><span class="ureact-glyph-module--icon-arrow-up-md--2UX1I ureact-glyph-module--icon--1oZQL" title=""><i></i></span></span><span data-test="menu" class="control-bar--menu-text--1XDF0">Menu</span></div><div class="control-bar--alertNotification--2nnvv"></div></div><div class="control-bar--left-group-lower--2vnx1"><noscript></noscript></div></div><div class="control-bar--gpu-meter--3G60H"><div class="control-bar--gpu-meter--label--3HlyD control-bar--running--1RYdn"><span class="control-bar--dot--2sEdT">•</span><span>GPU</span></div><div class="control-bar--gpu-meter--controls--3XzM_"><div class="control-bar--gpu-meter--time--1KN3U"><span class="control-bar--numbers--33u6H">46</span><span class="control-bar--text--1GkiN">HR</span><span class="control-bar--numbers--33u6H">31</span><span class="control-bar--text--1GkiN">MIN</span></div><div class="control-bar--gpu-meter--button--2kvzv">DISABLE</div></div></div></div><div class="control-bar--menu-right--2p1lH"><div class="control-bar--action-button--3sXJB"><span></span></div><div class="control-bar--finish-button--16CUd"><button type="button" class="index-module--secondary--wBQsM index-module--_btn--2sEaV  index-module--standard--2oyVV" style="cursor: pointer;">Next</button></div></div></div></div><div class="ReactModalPortal"></div><div class="ReactModalPortal"></div><div class="ReactModalPortal"></div><div class="ReactModalPortal"></div><div class="ReactModalPortal"></div><div class="ReactModalPortal"></div><div style="position: absolute; top: 0px; left: 0px; width: 100%;"><div><div class="rc-tooltip workspace-menu-tooltip rc-tooltip-placement-top  rc-tooltip-hidden" style="left: 17.3516px; top: 528px;"><div class="rc-tooltip-content"><div class="rc-tooltip-arrow"></div><div class="rc-tooltip-inner"><div class="menu-tooltip--menu--2N98_"><div><div class="menu-tooltip--item--1QFqg"><p data-test="urws-restore-backups" class="menu-tooltip--tooltip-button--2URnG">Restore a Backup...</p><div class="menu-tooltip--notification-container--3xE9r"></div></div><div class="menu-tooltip--separator--3NaNr"></div></div><div class="menu-tooltip--item--1QFqg"><p data-test="refresh-workspace" class="menu-tooltip--tooltip-button--2URnG">Refresh Workspace...</p><div class="menu-tooltip--notification-container--3xE9r"></div></div><div class="menu-tooltip--separator--3NaNr"></div><div class="menu-tooltip--item--1QFqg"><p data-test="reset-workspace" class="menu-tooltip--tooltip-button--2URnG">Reset Data...</p><div class="menu-tooltip--notification-container--3xE9r"></div></div></div></div></div></div></div></div></div></div><span></span></div></div></div></div><noscript></noscript><noscript></noscript></div></div></div></main></div></div></div></div></div></div></div></div><script src="./train_files/vendors_app.f5d09.js.download"></script><script src="./train_files/app.7d2cb.js.download"></script><iframe id="intercom-frame" style="position: absolute !important; opacity: 0 !important; width: 1px !important; height: 1px !important; top: 0 !important; left: 0 !important; border: none !important; display: block !important; z-index: -1 !important;" aria-hidden="true" tabindex="-1" title="Intercom" src="./train_files/saved_resource.html"></iframe><div id="intercom-css-container"><style data-emotion="intercom-global"></style><style data-emotion="intercom"></style></div><div id="intercom-container" class="intercom-namespace"><style>html.intercom-mobile-messenger-active,html.intercom-mobile-messenger-active > body,html.intercom-modal-open,#intercom-container-body{overflow:hidden !important;}html.intercom-mobile-messenger-active,html.intercom-mobile-messenger-active > body{position:static !important;}html.intercom-mobile-messenger-active > body{height:0 !important;margin:0 !important;}iframe#intercom-frame{position:absolute !important;opacity:0 !important;width:1px !important;height:1px !important;top:0 !important;left:0 !important;border:none !important;display:block !important;z-index:-1 !important;}</style><div class="intercom-app" aria-live="polite"><iframe allowfullscreen="" class="intercom-launcher-frame intercom-1p3djve e1ur5zlj0" name="intercom-launcher-frame" title="Intercom live chat" data-intercom-frame="true" src="./train_files/saved_resource(1).html"></iframe><div id="intercom-modal-container"></div></div></div><div id="modals-root" class="student-workspace scoped-bootstrap theme_light">
    <div id="files_modal" tabindex="-1" role="dialog" class="modal">
      <div class="modal-dialog">
        <button type="button" class="close modal-close" data-dismiss="modal" aria-hidden="true">×</button>
        <div class="modal-content">
          <div class="modal-body">
            <form id="files_modal_form" class="form-inline">
              <div id="files_modal_display" class="form-group">
                <div class="navbar">
                  <div class="modal--back-arrow"><li class="navigate_up"><a><span class="ureact-glyph-module--icon-arrow-left-sm--1Wem1 ureact-glyph-module--icon--1oZQL" title="Back"><i>Back</i></span></a></li></div>
                  <ul id="modal_crumbs" class="breadcrumbs"><li class="active">/</li></ul>
                </div>
                <div id="react-modal-container" class="files-modal-table-container"></div>
              </div>
              <div id="files_modal_name_select">
                <div class="files-modal--input">
                  <input id="files_modal_input" type="text" name="input" placeholder="Name" class="form-control field">
                </div>
                <div class="files-modal--submit">
                  <input id="files_modal_submit" type="submit" value="Open or Create" class="btn btn-primary">
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div id="confirm_modal" tabindex="-1" role="dialog" class="modal">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-body">
            <center>
              <p></p>
              <button id="confirm_no" data-dismiss="modal" class="btn btn-default">Cancel</button>
              <button id="confirm_yes" data-dismiss="modal" class="btn btn-primary">Confirm</button>
            </center>
          </div>
        </div>
      </div>
    </div>
    <div id="main_modal" tabindex="-1" role="dialog" class="modal">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-body"></div>
        </div>
      </div>
    </div>
    <div id="react-modal"></div>
  </div></body></html>