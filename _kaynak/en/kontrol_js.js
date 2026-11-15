const fs=require('fs'),vm=require('vm');
function load(p){const w={};const ctx={window:w,self:w,globalThis:w,document:{},console};vm.createContext(ctx);vm.runInContext(fs.readFileSync(p,'utf8'),ctx);const o={};for(const k of Object.keys(w))o[k]=w[k];for(const k of Object.keys(ctx))if(!['window','self','globalThis','document','console'].includes(k))o[k]=ctx[k];return o;}
const errs=[];
function cmp(a,b,p){const ta=Array.isArray(a)?'array':typeof a,tb=Array.isArray(b)?'array':typeof b;
 if(ta!==tb){errs.push(`${p}: ${ta} vs ${tb}`);return}
 if(ta==='array'){if(a.length!==b.length){errs.push(`${p}: len ${a.length} vs ${b.length}`);return}a.forEach((x,i)=>cmp(x,b[i],`${p}[${i}]`))}
 else if(ta==='object'&&a){const ka=Object.keys(a),kb=Object.keys(b);if(ka.join()!==kb.join()){errs.push(`${p}: keys differ`);return}ka.forEach(k=>cmp(a[k],b[k],`${p}.${k}`))}
 else if(ta!=='string'&&ta!=='function'&&a!==b)errs.push(`${p}: ${a} vs ${b}`)}
const A=load(process.argv[2]),B=load(process.argv[3]);cmp(A,B,'root');
console.log(errs.length?'ERRORS:\n'+errs.slice(0,60).join('\n'):'OK');
