$(document).on("click", ".open-UploadImageDialog", function () {
     var blogArticleId = $(this).data('id');
     $(".modal-body #blogArticleId").val( blogArticleId );
});
$(document).on("click", ".open-EditArticleDialog", function () {

     var blogArticleId = $(this).data('id');
     var title = $(this).data('title');
     var content = $('#blog_content').text(); // blog_content might be a lot of string, it's better not to duplicate in as element information

     $(".modal-body #editBlogArticleId").val( blogArticleId );
     $(".modal-body #editBlogArticleTitle").val( title );
     $(".modal-body #editBlogArticleContent").val( content );
});
 $(document).on("click", ".open-UploadImageDialog", function () {
     var blogArticleId = $(this).data('id');
     $(".modal-body #blogArticleId").val( blogArticleId );
});
 $(document).on("click", ".open-UploadImageDialog", function () {
     var blogArticleId = $(this).data('id');
     $(".modal-body #blogArticleId").val( blogArticleId );
});

function editarticlemodal(title, content){
    $("#editBlogArticleTitle").value = title;
    $("#editBlogArticleContent").value = content;

};
