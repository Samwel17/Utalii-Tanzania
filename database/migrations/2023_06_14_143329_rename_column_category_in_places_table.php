<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class RenameColumnCategoryInPlacesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('places', function (Blueprint $table) {
            $table->unsignedInteger("category_id")->change();

            // conditionally check if there's a column named category in the table and then change it accordingly
            // if (Schema::hasColumn('places', 'category')) {
            //     $table->renameColumn("category", "category_id");
            //     // change the column type to unsigned integer
            //     $table->unsignedInteger('category_id')->change();
            // } else {
            //     $table->unsignedInteger('category_id')->change('image');
            // }

            // $table->index(['category_id', 'places_category_id_fk_places_categories_idx']);

            // $table->foreign('category_id', 'fk_places_categories_idx')
            //     ->references('id')->on('categories')
            //     ->onDelete('no action')
            //     ->onUpdate('no action');

            // $table->foreign('category_id', 'places_category_id_foreign')
            //     ->references('id')->on('categories')
            //     ->onDelete('no action')
            //     ->onUpdate('no action');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('places', function (Blueprint $table) {
            //
        });
    }
}
