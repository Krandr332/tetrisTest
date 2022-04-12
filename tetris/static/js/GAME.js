var map=[], pos=5, move=0, score=0, bit=0, fig=0;
var canvas = document.querySelector('#canvas'),  ctx = canvas.getContext("2d");
function _$ (body, ret){ return eval("(function(a,b,c){"+(ret ? 'return ':'')+body+";})");}
_i = _$("parseInt(a)", 1);
range = _$("_$('for(var i='+a+'; i<='+b+'; ++i ) a(i); return 1')", 1);
set_color = _$("ctx.fillStyle = (['none', 'white', 'black', 'red'])[a]", 1);
draw_cell = _$("set_color(map[a]) && ctx.fillRect(a%10*20, _i(a/10)*20-20*3, 19, 19);");
can_move = _$("(b>1 || _i(a/10)==_i((a+b)/10)) && (a+b>=0) && ((a+b)<map.length) && (map[a+b]!=2)", 1);
bounced = _$('map.reduce(_$("a + ((b==3) && !can_move(c, "+a+")) ? 1 : 0", 1), 0)', 1);
cell_move = _$("can_move(a, b) && (map[a+b]=map[a]) && (map[a]=1)");
cell = _$("map[pos + a%4 + parseInt(a/4)*10] = (([1,15,46,78,142,204,198])[b] & (1<<(7-a))) ? 3 : 1");
new_fig = _$("range(0, 7)(_$('cell(a,'+(Math.floor(Math.random()*6)+1)+')'))", 1);
(rng0_229 = range(0, 229))(_$("map[a] = 1"));
new_fig();
document.body.onkeydown = function(e) {
    (move = ([-1, 0, 1, 10])[e.keyCode-37]) && !bounced(move)
       && rng0_229 (_$("b = move<0 ? a : 229-a; map[b]==3 && cell_move(b, move)"));
};
var interval = setInterval (function () {
    bounced(10) >0  && rng0_229 (_$("map[a]==3 && (map[a]=2)"))
         && range(3, 22) (_$('map.slice(a*10, a*10+10).reduce(_$("a+b", 1),0)==20 && ++score\
                             && range(a*10, a*10+9)(_$("map[a]=1"))\
                             && rng0_229 (_$("cell_move(229-a, 10)"))'))
         && range(20, 29) (_$("(map[a]==2) && interval && !clearInterval(interval) \
                          && !alert ('Game over! Score: '+score) && (interval=0) "))
       && new_fig();
    rng0_229 (_$("map[229-a]==3 && a>=10 && cell_move(229-a, 10)"))
    rng0_229 (_$("draw_cell(a)"))
}, 200);