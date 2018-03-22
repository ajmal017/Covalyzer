namespace Covalyzer.Ef
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("Watchlist")]
    public partial class Watchlist
    {
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int id { get; set; }

        public int member_map_id { get; set; }

        [StringLength(50)]
        public string name { get; set; }

        public virtual MemberMap MemberMap { get; set; }
    }
}
