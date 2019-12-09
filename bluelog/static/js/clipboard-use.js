/*页面载入完成后，创建复制按钮*/
!function (e, t, a) {
  /* code */
  var initCopyCode = function(){
    var copyHtml = '';
    copyHtml += '<button class="btn-copy" data-clipboard-snippet="">';
    copyHtml += '<i class="fa fa-clipboard"></i><span>copy</span>';
    copyHtml += '</button>';
    // 因为使用的是谷歌代码插件样式，每个pre标签外再嵌套一层code
    // $("pre").wrap("<code></code>");
    $("code").before(copyHtml).append;
    new ClipboardJS('.btn-copy', {
        target: function(trigger) {
            return trigger.nextElementSibling;
        }
    });
  }
  initCopyCode();
}(window, document);
