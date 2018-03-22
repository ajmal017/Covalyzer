namespace Covalyzer.Ef
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("MemberMap")]
    public partial class MemberMap
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public MemberMap()
        {
            Watchlist = new HashSet<Watchlist>();
        }

        [Key]
        [Column("int")]
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int _int { get; set; }

        public int watchlist_id { get; set; }

        public int security_id { get; set; }

        public int? position { get; set; }

        public virtual Security Security { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<Watchlist> Watchlist { get; set; }
    }
}
